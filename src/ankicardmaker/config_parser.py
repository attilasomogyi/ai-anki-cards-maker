"""This module provide for handle the configuration file."""
# pylint: disable=line-too-long

import json
from tomllib import load
from os.path import expanduser, isfile, join, dirname
from platform import system
from jsonschema import validate, Draft202012Validator


class ConfigParser:
    """Class providing a function to handle the configuration file."""

    def get_config_file(self):
        """Get the configuration file."""
        config_file_name = "ankicardmaker.toml"
        match system():
            case "Linux":
                config_file_path = f"{expanduser('~')}/.config/{config_file_name}"
            case "Darwin":
                config_file_path = (
                    f"{expanduser('~')}/Library/Application Support/{config_file_name}"
                )
            case "Windows":
                config_file_path = (
                    f"{expanduser('~')}\\AppData\\Roaming\\{config_file_name}"
                )
            case _:
                raise ValueError("Unsupported operating system")
        if not isfile(config_file_path):
            return None
        try:
            with open(config_file_path, "rb") as config_file:
                return load(config_file)
        except IOError as error:
            raise ValueError(f"Could not read {config_file_path}") from error

    def validate_config_file(self):
        """Validate the configuration file."""
        json_schema_path = join(
            dirname(__file__), "data", "ankicardmaker_config_file_schema.json"
        )
        if not isfile(json_schema_path):
            raise ValueError(f"{json_schema_path} does not exist.")
        with open(json_schema_path, "r", encoding="utf-8") as json_schema_file:
            try:
                schema = json.load(json_schema_file)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"{json_schema_path} is not a valid JSON file."
                ) from error
            if not schema:
                raise ValueError(f"{json_schema_path} is empty.")
            validate(
                instance=self.get_config_file(),
                schema=schema,
                format_checker=Draft202012Validator.FORMAT_CHECKER,
            )

"""This module provide for handle the configuration file."""
# pylint: disable=line-too-long
# flake8: noqa W503

import json
from tomllib import load
from pathlib import Path
from platform import system
from jsonschema import validate, Draft202012Validator


class ConfigParser:
    """Class providing a function to handle the configuration file."""

    def __init__(self):
        self.home_dir = Path.home()
        self.config_file_name = "ankicardmaker.toml"
        self.json_schema_path = (
            Path(__file__).parent / "data" / "ankicardmaker_config_file_schema.json"
        )
        self.json_schema = self.get_json_schema()

    def get_json_schema(self):
        """Get the JSON schema."""
        if not self.json_schema_path.is_file():
            raise ValueError(f"{self.json_schema_path} does not exist.")
        with open(self.json_schema_path, "r", encoding="utf-8") as json_schema_file:
            try:
                return json.load(json_schema_file)
            except json.JSONDecodeError as error:
                raise ValueError(
                    f"{self.json_schema_path} is not a valid JSON file."
                ) from error

    def get_config_file(self):
        """Get the configuration file."""
        match system():
            case "Linux":
                config_file_path = self.home_dir / ".config" / self.config_file_name
            case "Darwin":
                config_file_path = (
                    self.home_dir
                    / "Library"
                    / "Application Support"
                    / self.config_file_name
                )
            case "Windows":
                config_file_path = (
                    self.home_dir / "AppData" / "Roaming" / self.config_file_name
                )
            case _:
                raise ValueError("Unsupported operating system")
        if not config_file_path.is_file():
            return None
        try:
            with open(config_file_path, "rb") as config_file:
                return load(config_file)
        except IOError as error:
            raise ValueError(f"Could not read {config_file_path}") from error

    def validate_config_file(self):
        """Validate the configuration file."""
        if not self.json_schema:
            raise ValueError(f"{self.json_schema_path} is empty.")
        validate(
            instance=self.get_config_file(),
            schema=self.json_schema,
            format_checker=Draft202012Validator.FORMAT_CHECKER,
        )

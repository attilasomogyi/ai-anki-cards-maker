# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

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

    __slots__ = ("home_dir", "config_file_name", "json_schema_path", "json_schema")

    def __init__(self):
        self.home_dir = Path.home()
        self.config_file_name = "ankicardmaker.toml"
        self.json_schema_path = (
            Path(__file__).parent / "data" / "ankicardmaker_config_file_schema.json"
        )
        self.json_schema = self.get_json_schema()

    def get_json_schema(self) -> dict:
        """Get the JSON schema."""
        try:
            with open(self.json_schema_path, "r", encoding="utf-8") as json_schema_file:
                return json.load(json_schema_file)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            raise ValueError(
                f"{self.json_schema_path} {'does not exist' if isinstance(error, FileNotFoundError) else 'is not a valid JSON file'}."
            ) from error

    def get_config_file_path(self) -> Path:
        """Get the configuration file path."""
        paths = {
            "Linux": [".config"],
            "Darwin": ["Library", "Application Support"],
            "Windows": ["AppData", "Roaming"],
        }
        system_name = system()
        if system_name not in paths:
            raise ValueError("Unsupported operating system.")
        return self.home_dir / Path(*paths[system_name]) / self.config_file_name

    def get_config_file(self) -> dict | None:
        """Get the configuration file."""
        try:
            with open(self.get_config_file_path(), "rb") as config_file:
                return self.validate_config_file(load(config_file))
        except (IOError, FileNotFoundError) as error:
            if isinstance(error, FileNotFoundError):
                return None
            raise ValueError(f"Could not read {self.get_config_file_path()}") from error

    def validate_config_file(self, config_file: dict) -> dict:
        """Validate the configuration file."""
        if not self.json_schema:
            raise ValueError(f"{self.json_schema_path} is empty.")
        validate(
            instance=config_file,
            schema=self.json_schema,
            format_checker=Draft202012Validator.FORMAT_CHECKER,
        )
        return config_file

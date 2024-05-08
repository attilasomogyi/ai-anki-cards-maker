# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for providing the configuration file validator."""

from jsonschema import validate, Draft202012Validator
from ankicardmaker.modules.config.json_schema import ConfigJsonSchema
from ankicardmaker.modules.config.json_schema_path import ConfigJsonSchemaPath


# pylint: disable=too-few-public-methods
class ConfigFileValidator:
    """Class providing a function to validate the configuration file."""

    @staticmethod
    def validate(config_file: dict) -> dict:
        """Validate the configuration file."""
        json_schema = ConfigJsonSchema.get()
        json_schema_path = ConfigJsonSchemaPath.get()
        if not json_schema:
            raise ValueError(f"{json_schema_path} is empty.")
        validate(
            instance=config_file,
            schema=json_schema,
            format_checker=Draft202012Validator.FORMAT_CHECKER,
        )
        return config_file

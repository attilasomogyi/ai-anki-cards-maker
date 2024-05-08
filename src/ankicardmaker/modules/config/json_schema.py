# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""This module provide for handle the configuration file JSON schema."""

import json
from functools import cache
from ankicardmaker.modules.config.json_schema_path import ConfigJsonSchemaPath


# pylint: disable=too-few-public-methods
class ConfigJsonSchema:
    """Class providing a function to handle the configuration file JSON schema."""

    @staticmethod
    @cache
    def get() -> dict:
        """Get the configuration file JSON schema."""
        json_schema_path = ConfigJsonSchemaPath().get()
        try:
            with open(json_schema_path, "r", encoding="utf-8") as json_schema_file:
                return json.load(json_schema_file)
        except (FileNotFoundError, json.JSONDecodeError) as error:
            error_type = (
                "does not exist"
                if isinstance(error, FileNotFoundError)
                else "is not a valid JSON file"
            )
            error_message = f"{json_schema_path} {error_type}."
            raise ValueError(error_message) from error

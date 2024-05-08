# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for providing the path of the JSON schema."""

from pathlib import Path


# pylint: disable=too-few-public-methods
class ConfigJsonSchemaPath:
    """Class providing a function to get the path of the JSON schema."""

    @staticmethod
    def get() -> Path:
        """Get the path of the JSON schema."""
        return (
            Path(__file__).parent / "schema" / "ankicardmaker_config_file_schema.json"
        )

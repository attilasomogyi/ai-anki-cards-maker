# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to get the configuration file path."""

from pathlib import Path
from platform import system


# pylint: disable=too-few-public-methods
class ConfigFilePath:
    """Class providing a function to get the configuration file JSON schema path."""

    @staticmethod
    def get() -> Path:
        """Get the configuration file path."""
        paths = {
            "Linux": [".config"],
            "Darwin": ["Library", "Application Support"],
            "Windows": ["AppData", "Roaming"],
        }
        system_name = system()
        if system_name not in paths:
            raise ValueError("Unsupported operating system.")
        return Path.home() / Path(*paths[system_name]) / "ankicardmaker.toml"

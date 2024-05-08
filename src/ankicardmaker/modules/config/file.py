# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""This module provides the ConfigFile class."""

from tomllib import load
from functools import cache
from ankicardmaker.modules.config.file_path import ConfigFilePath
from ankicardmaker.modules.config.validator import ConfigFileValidator


# pylint: disable=too-few-public-methods
class ConfigFile:
    """Class providing a function to get the configuration file."""

    @staticmethod
    @cache
    def get() -> dict | None:
        """Get the configuration file."""
        config_file_path = ConfigFilePath().get()
        try:
            with open(config_file_path, "rb") as config_file:
                return ConfigFileValidator.validate(load(config_file))
        except (IOError, FileNotFoundError) as error:
            if isinstance(error, FileNotFoundError):
                return None
            raise ValueError(f"Could not read {config_file_path}") from error

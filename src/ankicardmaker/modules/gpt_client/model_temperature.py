# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to get OpenAI temperature."""

from functools import cache
from ankicardmaker.modules.config.file import ConfigFile


# pylint: disable=too-few-public-methods
class GPTClientModelTemperature:
    """Class providing a function to get OpenAI temperature."""

    @staticmethod
    @cache
    def get() -> float:
        """Get OpenAI temperature."""
        config = ConfigFile().get()
        if config is not None and "openai" in config:
            return config["openai"].get("temperature", 0.7)
        return 0.7

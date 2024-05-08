# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to get OpenAI API key."""

from functools import cache
from ankicardmaker.modules.config.file import ConfigFile


# pylint: disable=too-few-public-methods
class GPTClientAPIKey:
    """Class providing a function to get OpenAI API key."""

    @staticmethod
    @cache
    def get() -> str | None:
        """Get OpenAI API key."""
        config = ConfigFile().get()
        if config is not None and "openai" in config:
            return config["openai"].get("api_key", None)
        return None

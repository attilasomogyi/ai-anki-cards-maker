# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to get OpenAI model."""

from functools import cache
from ankicardmaker.modules.config.file import ConfigFile


# pylint: disable=too-few-public-methods
class GPTClientModel:
    """Class providing a function to get OpenAI model."""

    @staticmethod
    @cache
    def get() -> str:
        """Get OpenAI model."""
        config = ConfigFile().get()
        if config is not None and "openai" in config:
            return config["openai"].get("model", "gpt-4-0125-preview")
        return "gpt-4-0125-preview"

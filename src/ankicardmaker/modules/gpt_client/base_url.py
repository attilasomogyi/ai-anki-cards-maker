# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to get OpenAI client base URL."""

from functools import cache
from ankicardmaker.modules.config.file import ConfigFile


# pylint: disable=too-few-public-methods
class GPTClientBaseURL:
    """Class providing a function to get base URL."""

    @staticmethod
    @cache
    def get() -> str | None:
        """Get Open AI client base URL."""
        config = ConfigFile().get()
        if config is not None and "openai" in config:
            return config["openai"].get("base_url", None)
        return None

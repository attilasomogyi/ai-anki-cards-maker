# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to get Anki-Connect API key."""

from os import getenv
from functools import lru_cache
from ankicardmaker.modules.config.file import ConfigFile


# pylint: disable=too-few-public-methods
class AnkiConnectApiKey:
    """Class providing a function to get Anki-Connect API key."""

    @staticmethod
    @lru_cache
    def get():
        """Get Anki-Connect API key."""
        if getenv("ANKI_CONNECT_API_KEY") is not None:
            return getenv("ANKI_CONNECT_API_KEY")
        api_key = ConfigFile().get().get("anki_connect", {}).get("api_key")
        if api_key is not None:
            return api_key
        raise ValueError("ANKI_CONNECT_API_KEY is not set")

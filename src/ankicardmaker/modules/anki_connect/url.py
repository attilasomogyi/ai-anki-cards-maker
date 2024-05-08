# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to execute Anki request payloads."""

from functools import lru_cache
from ankicardmaker.modules.config.file import ConfigFile


# pylint: disable=too-few-public-methods
class AnkiConnectUrl:
    """Class providing a function to get Anki-Connect URL."""

    @staticmethod
    @lru_cache
    def get():
        """Get Anki-Connect URL."""
        return (
            ConfigFile()
            .get()
            .get("anki_connect", {})
            .get("url", "http://127.0.0.1:8765")
        )

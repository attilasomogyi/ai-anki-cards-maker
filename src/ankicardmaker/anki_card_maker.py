# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to create Anki cards."""

from json import dumps, load
import contextlib
from urllib.request import urlopen, Request
from os import getenv
from functools import lru_cache
from ankicardmaker.config_parser import ConfigParser


class AnkiCardMaker:
    """Class providing a function to create Anki cards."""

    __slots__ = ("config_parser", "anki_connect_api_key", "anki_connect_url")

    def __init__(self):
        self.config_parser = ConfigParser()
        self.anki_connect_api_key = self.get_anki_connect_api_key()
        self.anki_connect_url = self.get_anki_connect_url()

    @lru_cache(maxsize=1000)
    def get_anki_connect_api_key(self):
        """Get Anki-Connect API key."""
        if getenv("ANKI_CONNECT_API_KEY") is not None:
            return getenv("ANKI_CONNECT_API_KEY")
        api_key = (
            self.config_parser.get_config_file().get("anki_connect", {}).get("api_key")
        )
        if api_key is not None:
            return api_key
        raise ValueError("ANKI_CONNECT_API_KEY is not set")

    @lru_cache(maxsize=1000)
    def get_anki_connect_url(self):
        """Get Anki-Connect URL."""
        return (
            self.config_parser.get_config_file()
            .get("anki_connect", {})
            .get("url", "http://127.0.0.1:8765")
        )

    def create_request_payload(self, operation, **parameters) -> dict:
        """Create a request payload."""
        return {
            "action": operation,
            "params": parameters,
            "version": 6,
            "key": self.anki_connect_api_key,
        }

    def execute_operation(self, operation, **parameters):
        """Invoke an action."""
        request = Request(
            self.anki_connect_url,
            dumps(self.create_request_payload(operation, **parameters)).encode("utf-8"),
        )
        with contextlib.closing(urlopen(request)) as response:
            response = load(response)
            if response["error"] is not None:
                raise ValueError(response["error"].capitalize())

    def create_note(
        self, deck_name: str, front: str, back: str, allow_duplicates: bool = False
    ) -> dict:
        """Create a note."""
        if not (deck_name and front and back):
            raise ValueError("deckName, front and back are required.")
        return {
            "note": {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {"Front": front, "Back": back},
                "tags": ["ai-generated"],
                "options": {"allowDuplicate": allow_duplicates},
            }
        }

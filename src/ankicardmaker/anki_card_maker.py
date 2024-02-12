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

    @lru_cache
    def get_anki_connect_api_key(self):
        """Get Anki-Connect API key."""
        anki_connect_api_key = getenv("ANKI_CONNECT_API_KEY")
        if anki_connect_api_key is None:
            config_file = self.config_parser.get_config_file()
            anki_connect_api_key = config_file["anki_connect"]["api_key"]
            if anki_connect_api_key is None:
                raise ValueError("ANKI_CONNECT_API_KEY is not set")
        return anki_connect_api_key

    @lru_cache
    def get_anki_connect_url(self):
        """Get Anki-Connect URL."""
        config_file = self.config_parser.get_config_file()
        anki_connect_url = config_file["anki_connect"]["url"]
        if anki_connect_url:
            return anki_connect_url
        return "http://127.0.0.1:8765"

    def create_request_payload(self, operation, **parameters):
        """Create a request payload."""
        return {
            "action": operation,
            "params": parameters,
            "version": 6,
            "key": self.anki_connect_api_key,
        }

    def execute_operation(self, operation, **parameters):
        """Invoke an action."""
        request_json = dumps(
            self.create_request_payload(operation, **parameters)
        ).encode("utf-8")
        request = Request(self.anki_connect_url, request_json)
        with contextlib.closing(urlopen(request)) as response:
            response = load(response)
            if response["error"] is not None:
                raise ValueError(response["error"].capitalize())

    def create_note(self, deck_name, front, back, allow_duplicates=False):
        """Create a note."""
        if not deck_name or not front or not back:
            raise ValueError("deckName, front and back are required")

        note = {
            "note": {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {"Front": front, "Back": back},
                "tags": ["ai-generated"],
            }
        }

        if allow_duplicates:
            note["note"]["options"] = {"allowDuplicate": True}

        return note

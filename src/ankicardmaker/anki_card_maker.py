"""Module providing a function to create Anki cards."""

from json import dumps, load
import contextlib
from urllib.request import urlopen, Request
from os import getenv


class AnkiCardMaker:
    """Class providing a function to create Anki cards."""

    def __init__(self):
        self.anki_connect_api_key = self.get_anki_connect_api_key()
        self.anki_connect_url = "http://127.0.0.1:8765"

    def get_anki_connect_api_key(self):
        """Get Anki-Connect API key."""
        anki_connect_api_key = getenv("ANKI_CONNECT_API_KEY")
        if anki_connect_api_key is None:
            raise ValueError("ANKI_CONNECT_API_KEY environment variable is not set")
        return anki_connect_api_key

    def create_request(self, action, **params):
        """Create a request object."""
        return {
            "action": action,
            "params": params,
            "version": 6,
            "key": self.anki_connect_api_key,
        }

    def invoke(self, action, **params):
        """Invoke an action."""
        request_json = dumps(self.create_request(action, **params)).encode("utf-8")
        request = Request(self.anki_connect_url, request_json)
        with contextlib.closing(urlopen(request)) as response:
            response = load(response)
        if len(response) != 2:
            raise ValueError("response has an unexpected number of fields")
        if "error" not in response:
            raise ValueError("response is missing required error field")
        if "result" not in response:
            raise ValueError("response is missing required result field")
        return response["result"]

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

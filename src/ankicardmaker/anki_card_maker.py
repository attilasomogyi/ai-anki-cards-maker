"""Module providing a function to create Anki cards."""

from json import dumps, load
from urllib.request import urlopen, Request
from os import getenv


class AnkiCardMaker:
    """Class providing a function to create Anki cards."""

    def __init__(self):
        try:
            self.api_key = getenv("ANKI_API_KEY")
        except Exception as e:
            raise ValueError("ANKI_API_KEY environment variable is not set") from e
        self.url = "http://127.0.0.1:8765"

    def request(self, action, **params):
        """Create a request object."""
        return {"action": action, "params": params, "version": 6, "key": self.api_key}

    def invoke(self, action, **params):
        """Invoke an action."""
        request_json = dumps(self.request(action, **params)).encode("utf-8")
        with urlopen(Request(self.url, request_json)) as response:
            response = load(response)
        if len(response) != 2:
            raise ValueError("response has an unexpected number of fields")
        if "error" not in response:
            raise ValueError("response is missing required error field")
        if "result" not in response:
            raise ValueError("response is missing required result field")
        return response["result"]

    def make_note(self, deck_name, front, back, allow_duplicates=False):
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

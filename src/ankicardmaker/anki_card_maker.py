from json import dumps, load
from urllib.request import urlopen, Request
from os import getenv
import socket

class AnkiCardMaker:
    def __init__(self):
        try:
            self.api_key = getenv('ANKI_API_KEY')
        except:
            raise Exception('ANKI_API_KEY environment variable is not set')
            exit(1)
        self.url = "http://127.0.0.1:8765"

    def request(self, action, **params):
        return {'action': action, 'params': params, 'version': 6, 'key': self.api_key}

    def invoke(self, action, **params):
        request_json = dumps(self.request(action, **params)).encode('utf-8')
        response = load(urlopen(Request(self.url, request_json)))        
        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        return response['result']

    def make_note(self, deck_name, front, back, allow_duplicates=False):
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
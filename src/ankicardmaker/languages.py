"""Module for handling languages and their codes."""

from json import load
from os import path


class Language:
    """Class providing a function to handle languages and their codes."""

    def __init__(self):
        data_path = path.join(path.dirname(__file__), "data", "language_codes.json")
        with open(data_path, "r", encoding="utf-8") as language_codes_json_file:
            self.languages = load(language_codes_json_file)

    def get_language_codes(self):
        """Get language codes."""
        language_list = []
        for language in self.languages:
            language_list.append(language["code"])
        return language_list

    def get_language_name(self, language_code):
        """Get language name."""
        for language in self.languages:
            if language["code"] == language_code:
                return language["name"]
        return None

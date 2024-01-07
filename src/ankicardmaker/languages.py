"""Module for handling languages and their codes."""

from json import load, JSONDecodeError
from os import path


class Language:
    """Class providing a function to handle languages and their codes."""

    def __init__(self):
        data_path = path.join(path.dirname(__file__), "data", "language_codes.json")
        if not path.exists(data_path):
            raise FileNotFoundError(f"{data_path} does not exist.")
        with open(data_path, "r", encoding="utf-8") as language_codes_json_file:
            try:
                self.languages = load(language_codes_json_file)
            except JSONDecodeError as error:
                raise ValueError(f"{data_path} is not a valid JSON file.") from error
            if not self.languages:
                raise ValueError(f"{data_path} is empty.")

    def get_language_codes(self):
        """Get language codes."""
        language_list = []
        for language in self.languages:
            language_list.append(language["code"])
        return language_list

    def get_language_name(self, language_code):
        """Get language name."""
        if not isinstance(language_code, str):
            raise TypeError("language_code must be a string.")
        for language in self.languages:
            if language["code"] == language_code:
                return language["name"]
        return None

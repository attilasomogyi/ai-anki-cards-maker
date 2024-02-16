"""Module for handling languages and their codes."""

from json import load
from os import path


class Language:
    """Class providing a function to handle languages and their codes."""

    __slots__ = ("languages", "language_dictionary")

    def __init__(self):
        self.languages = self.get_languages()
        self.language_dictionary = self.get_language_dictionary()

    def get_language_dictionary(self):
        """Get language dictionary."""
        return {language["code"]: language["name"] for language in self.languages}

    def get_languages(self):
        """Get languages."""
        data_path = path.join(path.dirname(__file__), "data", "language_codes.json")
        if not path.exists(data_path):
            raise FileNotFoundError(f"{data_path} does not exist.")
        with open(data_path, "r", encoding="utf-8") as language_codes_json_file:
            return load(language_codes_json_file)

    def get_language_codes(self):
        """Get language codes."""
        return [language["code"] for language in self.languages]

    def get_language_name(self, language_code):
        """Get language name."""
        return (
            self.language_dictionary.get(language_code)
            if isinstance(language_code, str)
            else None
        )

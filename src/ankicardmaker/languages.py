"""Module for handling languages and their codes."""

from json import load


class Language:
    """Class providing a function to handle languages and their codes."""

    def __init__(self):
        with open("language_codes.json", encoding="utf-8") as language_codes_json_file:
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

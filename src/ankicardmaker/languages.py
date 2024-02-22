# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling languages and their codes."""

from json import load
from os import path


class Language:
    """Class providing a function to handle languages and their codes."""

    __slots__ = ("languages", "language_dictionary")

    def __init__(self):
        self.languages = self.get_languages()
        self.language_dictionary = self.get_language_dictionary()

    def get_language_dictionary(self) -> dict:
        """Get language dictionary."""
        return {language["code"]: language["name"] for language in self.languages}

    def get_languages(self) -> list[dict]:
        """Get languages."""
        data_path = path.join(path.dirname(__file__), "data", "language_codes.json")
        if not path.exists(data_path):
            raise FileNotFoundError(f"{data_path} does not exist.")
        with open(data_path, "r", encoding="utf-8") as language_codes_json_file:
            return load(language_codes_json_file)

    def get_language_codes(self) -> list[str]:
        """Get language codes."""
        return [language["code"] for language in self.languages]

    def get_language_name(self, language_code) -> str | None:
        """Get language name."""
        return self.language_dictionary.get(language_code)

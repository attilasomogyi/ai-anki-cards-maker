# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling languages and their codes."""

from os import path
from json import load
from functools import cache


# pylint: disable=too-few-public-methods
class LanguageLanguages:
    """Class providing a function to get languages."""

    @staticmethod
    @cache
    def get() -> list[dict]:
        """Get languages."""
        data_path = path.join(path.dirname(__file__), "codes", "language_codes.json")
        if not path.exists(data_path):
            raise FileNotFoundError(f"{data_path} does not exist.")
        with open(data_path, "r", encoding="utf-8") as language_codes_json_file:
            return load(language_codes_json_file)

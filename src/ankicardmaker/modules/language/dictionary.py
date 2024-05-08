# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling languages and their codes."""

from functools import cache
from ankicardmaker.modules.language.languages import LanguageLanguages


# pylint: disable=too-few-public-methods
class LanguageDictionary:
    """Class providing a function to get language dictionary."""

    @staticmethod
    @cache
    def get() -> dict:
        """Get language dictionary."""
        return {
            language["code"]: language["name"] for language in LanguageLanguages().get()
        }

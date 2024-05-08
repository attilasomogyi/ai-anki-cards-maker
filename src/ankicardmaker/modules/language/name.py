# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling language names."""

from functools import cache
from ankicardmaker.modules.language.dictionary import LanguageDictionary


# pylint: disable=too-few-public-methods
class LanguageName:
    """Class providing a function to get language name."""

    @staticmethod
    @cache
    def get(language_code) -> str | None:
        """Get language name."""
        return LanguageDictionary().get().get(language_code)

# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling language codes."""

from functools import cache
from ankicardmaker.modules.language.languages import LanguageLanguages


# pylint: disable=too-few-public-methods
class LanguageCodes:
    """Class providing a function to get language codes."""

    @staticmethod
    @cache
    def get() -> list[str]:
        """Get language codes."""
        return [language["code"] for language in LanguageLanguages().get()]

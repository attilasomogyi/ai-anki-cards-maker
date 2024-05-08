# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling worker arguments."""


# pylint: disable=too-few-public-methods
class WorkerArguments:
    """Class providing a function to test the arguments."""

    @staticmethod
    def test(clipboard: str, deck_name: str, language_code: str) -> bool:
        """Test the arguments."""
        if not clipboard:
            raise TypeError("Clipboard content must be a non-empty string.")
        if not deck_name:
            raise TypeError("Deck name must be a non-empty string.")
        if not language_code:
            raise TypeError("Language code must be a non-empty string.")
        return True

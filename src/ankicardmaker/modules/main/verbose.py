# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling main verbose mode."""


# pylint: disable=too-few-public-methods
class MainVerbose:
    """Class providing a function to handle verbose mode."""

    @staticmethod
    def print(deck_name: str, section: str):
        """Print verbose."""
        print(f"Deck name: {deck_name}")
        print(f"Processing section:\n{section}\n")

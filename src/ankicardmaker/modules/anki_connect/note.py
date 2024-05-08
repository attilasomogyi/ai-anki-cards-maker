# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to create Anki notes."""


# pylint: disable=too-few-public-methods
class AnkiConnectNote:
    """Class providing a function to create Anki notes."""

    @staticmethod
    def create(deck_name: str, front: str, back: str) -> dict:
        """Create a note."""
        if not (deck_name and front and back):
            raise ValueError("deckName, front and back are required.")
        return {
            "note": {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {"Front": front, "Back": back},
                "tags": ["ai-generated"],
                "options": {"allowDuplicate": False},
            }
        }

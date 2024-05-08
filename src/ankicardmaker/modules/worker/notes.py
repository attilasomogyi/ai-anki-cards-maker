# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling worker notes."""

from ankicardmaker.modules.anki_connect.note import AnkiConnectNote


# pylint: disable=too-few-public-methods
class WorkerNotes:
    """Worker notes class."""

    @staticmethod
    def create(deck_name: str, gpt_response: dict):
        """Create notes."""
        for card in gpt_response["flashcards"]:
            if "question" not in card or "answer" not in card:
                raise ValueError("Invalid flashcard.")
            try:
                note = AnkiConnectNote.create(
                    deck_name, front=card["question"], back=card["answer"]
                )
                yield note
            except ValueError as error:
                raise ValueError(f"Failed to add note: {error}") from error

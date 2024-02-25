# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Worker module for the Anki Card Maker application."""

from functools import lru_cache
from pprint import pprint
from ankicardmaker.gpt_client import GPTClient
from ankicardmaker.anki_card_maker import AnkiCardMaker


class Worker:
    """Worker class for the Anki Card Maker application."""

    __slots__ = ("gpt", "anki", "verbose")

    def __init__(self, verbose: bool = False):
        self.gpt = GPTClient()
        self.anki = AnkiCardMaker()
        self.verbose = verbose

    def print_verbose(self, section: dict):
        """Print verbose."""
        if self.verbose:
            print("GPT response:")
            pprint(section)
            print()

    @lru_cache(maxsize=1)
    def get_cached_gpt_response(self, prompt: str) -> dict:
        """Get a GPT cached response."""
        if not prompt:
            raise ValueError("Prompt must be a non-empty string.")
        try:
            gpt_response = self.gpt.get_gpt_response(prompt)
        except ValueError as error:
            raise ValueError(f"Failed to get GPT response: {error}") from error
        if "flashcards" not in gpt_response:
            raise ValueError("No flashcards were generated.")
        return gpt_response

    def check_arguments(
        self, clipboard: str, deck_name: str, language_code: str
    ) -> bool:
        """Check the arguments."""
        if not clipboard:
            raise TypeError("Clipboard content must be a non-empty string.")
        if not deck_name:
            raise TypeError("Deck name must be a non-empty string.")
        if not language_code:
            raise TypeError("Language code must be a non-empty string.")
        return True

    def create_notes(self, deck_name: str, gpt_response: dict):
        """Create notes."""
        for card in gpt_response["flashcards"]:
            if "question" not in card or "answer" not in card:
                raise ValueError("Invalid flashcard.")
            try:
                note = self.anki.create_note(
                    deck_name, front=card["question"], back=card["answer"]
                )
                yield note
            except ValueError as error:
                raise ValueError(f"Failed to add note: {error}") from error

    def add_notes_to_anki(self, notes: list):
        """Create notes in Anki."""
        if not notes:
            raise ValueError("No notes to add.")
        for note in notes:
            try:
                self.anki.execute_operation("addNote", **note)
            except ValueError as error:
                raise ValueError(f"Failed to add note: {error}") from error

    def run(self, clipboard: str, deck_name: str, language_code: str):
        """Worker function."""
        self.check_arguments(clipboard, deck_name, language_code)
        prompt = self.gpt.create_prompt(clipboard, language_code)
        gpt_response = self.get_cached_gpt_response(prompt)
        self.print_verbose(gpt_response)
        try:
            notes = self.create_notes(deck_name, gpt_response)
        except ValueError as error:
            raise ValueError(f"Failed to create notes: {error}") from error
        self.add_notes_to_anki(notes)

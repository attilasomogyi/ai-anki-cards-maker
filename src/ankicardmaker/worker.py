"""Worker module for the Anki Card Maker application."""

from functools import lru_cache
from ankicardmaker.gpt_client import GPTClient
from ankicardmaker.anki_card_maker import AnkiCardMaker


class Worker:
    """Worker class for the Anki Card Maker application."""

    def __init__(self):
        self.gpt = GPTClient()
        self.anki = AnkiCardMaker()

    @lru_cache(maxsize=1000)
    def get_cached_gpt_response(self, prompt):
        """Get a GPT cached response."""
        if not isinstance(prompt, str) or not prompt:
            raise ValueError("Prompt is required")
        try:
            gpt_response = self.gpt.get_gpt_response(prompt)
        except ValueError as error:
            raise ValueError(f"Failed to get GPT response: {error}") from error
        if "flashcards" not in gpt_response:
            raise ValueError("No flashcards were generated.")
        return gpt_response

    def check_arguments(self, clipboard, deck_name, language_code):
        """Check the arguments."""
        if not isinstance(clipboard, str) or not clipboard:
            raise TypeError("Clipboard content must be a non-empty string")
        if not isinstance(deck_name, str) or not deck_name:
            raise TypeError("Deck name must be a non-empty string")
        if not isinstance(language_code, str) or not language_code:
            raise TypeError("Language code must be a non-empty string")
        return True

    def create_notes(self, deck_name, gpt_response):
        """Create notes."""
        notes = []
        for card in gpt_response["flashcards"]:
            if "question" not in card or "answer" not in card:
                raise ValueError("Invalid flashcard.")
            try:
                note = self.anki.create_note(
                    deck_name, front=card["question"], back=card["answer"]
                )
                notes.append(note)
            except ValueError as error:
                raise ValueError(f"Failed to add note: {error}") from error
        return notes

    def add_notes_to_anki(self, notes):
        """Create notes in Anki."""
        if isinstance(notes, list) and not notes:
            raise ValueError("No notes to add")
        for note in notes:
            try:
                self.anki.execute_operation("addNote", **note)
            except ValueError as error:
                raise ValueError(f"Failed to add note: {error}") from error

    def run(self, clipboard, deck_name, language_code):
        """Worker function."""
        self.check_arguments(clipboard, deck_name, language_code)
        prompt = self.gpt.create_prompt(clipboard, language_code)
        gpt_response = self.get_cached_gpt_response(prompt)
        try:
            notes = self.create_notes(deck_name, gpt_response)
        except ValueError as error:
            raise ValueError(f"Failed to create notes: {error}") from error
        self.add_notes_to_anki(notes)

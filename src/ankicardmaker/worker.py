"""Worker module for the Anki Card Maker application."""


from functools import lru_cache
from ankicardmaker.gpt_client import GPTClient
from ankicardmaker.anki_card_maker import AnkiCardMaker

gpt = GPTClient()
anki = AnkiCardMaker()


@lru_cache(maxsize=1000)
def cached_gpt_response(prompt):
    """Get a GPT response."""
    return gpt.get_gpt_response(prompt)


async def worker(clipboard, deck_name, language_code):
    """Worker function."""
    if not isinstance(clipboard, str) or not clipboard:
        raise TypeError("Clipboard content must be a non-empty string")

    if not isinstance(deck_name, str) or not deck_name:
        raise TypeError("Deck name must be a non-empty string")

    if not isinstance(language_code, str) or not language_code:
        raise TypeError("Language code must be a non-empty string")

    prompt = gpt.create_prompt(clipboard, language_code)
    try:
        response = cached_gpt_response(prompt)
    except ValueError as error:
        raise ValueError(f"Failed to get GPT response: {error}") from error

    if "flashcards" not in response:
        raise ValueError("No flashcards were generated.")

    notes = []
    for card in response["flashcards"]:
        if "question" not in card or "answer" not in card:
            raise ValueError("Invalid flashcard.")

        try:
            note = anki.create_note(
                deck_name, front=card["question"], back=card["answer"]
            )
            notes.append(note)
        except ValueError as error:
            raise ValueError(f"Failed to add note: {error}") from error

    for note in notes:
        try:
            anki.execute_operation("addNote", **note)
        except ValueError as error:
            raise ValueError(f"Failed to add note: {error}") from error

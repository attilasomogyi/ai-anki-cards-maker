"""Worker module for the Anki Card Maker application."""

from ankicardmaker.gpt_client import GPTClient
from ankicardmaker.anki_card_maker import AnkiCardMaker


async def worker(clipboard, deck_name, language_code):
    """Worker function."""
    gpt = GPTClient()
    if not clipboard:
        raise ValueError("Clipboard content is required")
    prompt = gpt.create_prompt(clipboard, language_code)
    response = gpt.get_gpt_response(prompt)
    anki = AnkiCardMaker()

    for card in response["flashcards"]:
        note = anki.make_note(deck_name, front=card["question"], back=card["answer"])
        anki.invoke("addNote", **note)

import pytest
from anki_card_maker import AnkiCardMaker

def test_make_note():
    # Arrange
    anki_card_maker = AnkiCardMaker()
    deck_name = 'TestDeck'
    front = 'TestFront'
    back = 'TestBack'
    allow_duplicates = True

    expected_note = {
        "note": {
            "deckName": deck_name,
            "modelName": "Basic",
            "fields": {"Front": front, "Back": back},
            "tags": ["ai-generated"],
            "options": {"allowDuplicate": True}
        }
    }

    # Act
    note = anki_card_maker.make_note(deck_name, front, back, allow_duplicates)

    # Assert
    assert note == expected_note
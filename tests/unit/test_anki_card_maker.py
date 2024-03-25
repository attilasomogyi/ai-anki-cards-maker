# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for AnkiCardMaker."""

from unittest.mock import patch, MagicMock
import json
import pytest
from ankicardmaker.anki_card_maker import AnkiCardMaker

# pylint: disable=protected-access
# flake8: noqa: W503


class TestAnkiCardMaker:
    """Test class for AnkiCardMaker."""

    def test_init(self):
        """Test __init__."""
        anki_card_maker = AnkiCardMaker()
        assert anki_card_maker._AnkiCardMaker__anki_connect is not None

    def test_get_anki_connect_api_key(self):
        """Test get_anki_connect_api_key."""
        with patch("ankicardmaker.anki_card_maker.getenv", return_value="api_key"):
            anki_card_maker = AnkiCardMaker()
            assert (
                anki_card_maker._AnkiCardMaker__get_anki_connect_api_key() == "api_key"
            )

    def test_get_anki_connect_api_key_error_none(self):
        """Test get_anki_connect_api_key."""
        with patch("ankicardmaker.anki_card_maker.getenv", return_value=None):
            with patch(
                "ankicardmaker.anki_card_maker.ConfigParser.get_config_file",
                return_value={"anki_connect": {"api_key": None}},
            ):
                with pytest.raises(ValueError):
                    AnkiCardMaker()

    def test_get_anki_connect_url(self):
        """Test get_anki_connect_url."""
        anki_card_maker = AnkiCardMaker()
        assert (
            anki_card_maker._AnkiCardMaker__get_anki_connect_url()
            == "http://127.0.0.1:8765"
        )

    def test_create_request_payload(self):
        """Test create_request_payload."""
        anki_card_maker = AnkiCardMaker()
        test_payload = {
            "action": "operation",
            "params": {"key": "value"},
            "version": 6,
            "key": anki_card_maker._AnkiCardMaker__anki_connect.api_key,
        }
        result = anki_card_maker._AnkiCardMaker__create_request_payload(
            "operation", key="value"
        )
        assert result == test_payload

    @patch("ankicardmaker.anki_card_maker.urlopen")
    def test_execute_operation(self, urlopen_mock):
        """Test execute_operation."""
        anki_card_maker = AnkiCardMaker()
        urlopen_mock.return_value = MagicMock()
        urlopen_mock.return_value.read.return_value = json.dumps(
            {"result": "result", "error": None}
        )
        assert anki_card_maker.execute_operation("operation", key="value") == "result"

    @patch("ankicardmaker.anki_card_maker.urlopen")
    def test_execute_operation_error(self, urlopen_mock):
        """Test execute_operation."""
        anki_card_maker = AnkiCardMaker()
        urlopen_mock.return_value = MagicMock()
        urlopen_mock.return_value.read.return_value = json.dumps(
            {"result": None, "error": "error"}
        )
        with pytest.raises(ValueError):
            anki_card_maker.execute_operation("operation", key="value")

    # pylint: disable=duplicate-code
    def test_create_note(self):
        """Test create_note."""
        anki_card_maker = AnkiCardMaker()
        deck_name = "Test Deck"
        front = "Test Front"
        back = "Test Back"
        result = anki_card_maker.create_note(deck_name, front, back)
        assert result == {
            "note": {
                "deckName": deck_name,
                "modelName": "Basic",
                "fields": {"Front": front, "Back": back},
                "tags": ["ai-generated"],
                "options": {"allowDuplicate": False},
            }
        }

    def test_create_note_missing_args(self):
        """Test create_note with missing arguments."""
        anki_card_maker = AnkiCardMaker()
        with pytest.raises(ValueError):
            anki_card_maker.create_note("", "Test Front", "Test Back")
        with pytest.raises(ValueError):
            anki_card_maker.create_note("Test Deck", "", "Test Back")
        with pytest.raises(ValueError):
            anki_card_maker.create_note("Test Deck", "Test Front", "")

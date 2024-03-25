# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for the CommandLine class."""


from unittest.mock import patch, MagicMock
from ankicardmaker.commandline import CommandLine

# pylint: disable=unused-argument, protected-access


class TestCommandLine:
    """Test class for CommandLine."""

    def test_init(self):
        """Test __init__."""
        command_line = CommandLine()
        assert command_line._CommandLine__language is not None

    def test_add_version_argument(self):
        """Test __add_version_argument."""
        command_line = CommandLine()
        parser = MagicMock()
        command_line._CommandLine__add_version_argument(parser)
        parser.add_argument.assert_called_once_with(
            "--version", action="version", version="%(prog)s 0.1"
        )

    def test_add_verbose_argument(self):
        """Test __add_verbose_argument."""
        command_line = CommandLine()
        parser = MagicMock()
        command_line._CommandLine__add_verbose_argument(parser)
        parser.add_argument.assert_called_once_with(
            "-v",
            "--verbose",
            dest="verbose",
            help="Verbose mode",
            action="store_true",
            required=False,
        )

    def test_add_deck_name_argument(self):
        """Test __add_deck_name_argument."""
        command_line = CommandLine()
        parser = MagicMock()
        command_line._CommandLine__add_deck_name_argument(parser)
        parser.add_argument.assert_called_once_with(
            "-d",
            "--deck",
            dest="deck_name",
            help="Deck name",
            required=True,
            nargs=1,
            type=str,
        )

    def test_add_language_argument(self):
        """Test __add_language_argument."""
        command_line = CommandLine()
        parser = MagicMock()
        command_line._CommandLine__add_language_argument(parser)
        parser.add_argument.assert_called_once_with(
            "-l",
            "--language",
            dest="language_code",
            help="Language code",
            choices=command_line._CommandLine__language.get_language_codes(),
            nargs=1,
            type=str,
        )

    def test_add_file_argument(self):
        """Test __add_file_argument."""
        command_line = CommandLine()
        parser = MagicMock()
        command_line._CommandLine__add_file_argument(parser)
        parser.add_argument.assert_called_once_with(
            "-f",
            "--file",
            dest="file_path",
            help="File path",
            required=False,
            nargs=1,
            type=str,
        )

    def test_get_parser_args(self):
        """Test __get_parser_args."""
        command_line = CommandLine()
        parser = command_line._CommandLine__get_parser_args()
        assert parser is not None
        assert parser._actions is not None
        assert parser.description == "Anki Card Maker"

    def test_get_parse_args(self):
        """Test get_parse_args."""
        mock_args = MagicMock()
        mock_args.language_code = None
        with patch("argparse.ArgumentParser.parse_args", return_value=mock_args):
            command_line = CommandLine()
            args = command_line.get_parse_args()
            assert args.language_code == "en"

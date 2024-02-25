# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to handle command line arguments."""

from argparse import ArgumentParser
from ankicardmaker.languages import Language


class CommandLine:
    """Class providing a function to handle command line arguments."""

    __slots__ = ("language", "parser")

    def __init__(self):
        self.language = Language()
        self.parser = self.get_parser_args()

    def add_version_argument(self, parser: ArgumentParser):
        """Add version argument."""
        parser.add_argument("--version", action="version", version="%(prog)s 0.1")

    def add_verbose_argument(self, parser: ArgumentParser):
        """Add verbose argument."""
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            help="Verbose mode",
            action="store_true",
            required=False,
        )

    def add_deck_name_argument(self, parser: ArgumentParser):
        """Add deck name argument."""
        parser.add_argument(
            "-d",
            "--deck",
            dest="deck_name",
            help="Deck name",
            required=True,
            nargs=1,
            type=str,
        )

    def add_language_argument(self, parser: ArgumentParser):
        """Add language argument."""
        parser.add_argument(
            "-l",
            "--language",
            dest="language_code",
            help="Language code",
            choices=self.language.get_language_codes(),
            nargs=1,
            type=str,
        )

    def add_file_argument(self, parser: ArgumentParser):
        """Add file argument."""
        parser.add_argument(
            "-f",
            "--file",
            dest="file_path",
            help="File path",
            required=False,
            nargs=1,
            type=str,
        )

    def get_parser_args(self) -> ArgumentParser:
        """Get command line arguments."""
        parser = ArgumentParser(description="Anki Card Maker")
        self.add_version_argument(parser)
        self.add_verbose_argument(parser)
        self.add_deck_name_argument(parser)
        self.add_language_argument(parser)
        self.add_file_argument(parser)
        return parser

    def get_parse_args(self) -> ArgumentParser:
        """Parse command line arguments."""
        parse = self.parser.parse_args()
        parse.language_code = parse.language_code or "en"
        return parse

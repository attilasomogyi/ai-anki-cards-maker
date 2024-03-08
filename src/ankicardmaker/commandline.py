# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module providing a function to handle command line arguments."""

from argparse import ArgumentParser
from ankicardmaker.languages import Language


# pylint: disable=too-few-public-methods
class CommandLine:
    """Class providing a function to handle command line arguments."""

    __slots__ = ("__language", "__parser")

    def __init__(self):
        self.__language = Language()
        self.__parser = self.__get_parser_args()

    def __add_version_argument(self, parser: ArgumentParser):
        """Add version argument."""
        parser.add_argument("--version", action="version", version="%(prog)s 0.1")

    def __add_verbose_argument(self, parser: ArgumentParser):
        """Add verbose argument."""
        parser.add_argument(
            "-v",
            "--verbose",
            dest="verbose",
            help="Verbose mode",
            action="store_true",
            required=False,
        )

    def __add_deck_name_argument(self, parser: ArgumentParser):
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

    def __add_language_argument(self, parser: ArgumentParser):
        """Add language argument."""
        parser.add_argument(
            "-l",
            "--language",
            dest="language_code",
            help="Language code",
            choices=self.__language.get_language_codes(),
            nargs=1,
            type=str,
        )

    def __add_file_argument(self, parser: ArgumentParser):
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

    def __get_parser_args(self) -> ArgumentParser:
        """Get command line arguments."""
        parser = ArgumentParser(description="Anki Card Maker")
        self.__add_version_argument(parser)
        self.__add_verbose_argument(parser)
        self.__add_deck_name_argument(parser)
        self.__add_language_argument(parser)
        self.__add_file_argument(parser)
        return parser

    def get_parse_args(self) -> ArgumentParser:
        """Parse command line arguments."""
        parse = self.__parser.parse_args()
        parse.language_code = parse.language_code or "en"
        return parse

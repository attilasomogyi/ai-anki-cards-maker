"""Module providing a function to handle command line arguments."""

from argparse import ArgumentParser
from ankicardmaker.languages import Language


class CommandLine:
    """Class providing a function to handle command line arguments."""

    def __init__(self):
        self.parser = self.get_parser_args()

    def get_parser_args(self):
        """Get command line arguments."""
        parser = ArgumentParser(description="Anki Card Maker")
        parser.add_argument("--version", action="version", version="%(prog)s 0.1")
        parser.add_argument(
            "-d",
            "--deck",
            dest="deck_name",
            help="Deck name",
            required=True,
            nargs=1,
            type=str,
        )
        language = Language()
        parser.add_argument(
            "-l",
            "--language",
            dest="language_code",
            help="Language code",
            choices=language.get_language_codes(),
            nargs=1,
            type=str,
        )
        parser.add_argument(
            "-f",
            "--file",
            dest="file_path",
            help="File path",
            required=False,
            nargs=1,
            type=str,
        )
        return parser

    def get_parse_args(self):
        """Parse command line arguments."""
        return self.parser.parse_args()

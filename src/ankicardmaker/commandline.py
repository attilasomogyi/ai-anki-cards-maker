"""Module providing a function to handle command line arguments."""

import argparse
from ankicardmaker.languages import Language


class CommandLine:
    """Class providing a function to handle command line arguments."""

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Anki Card Maker")
        self.parser.add_argument("--version", action="version", version="%(prog)s 0.1")
        self.parser.add_argument(
            "-d", "--deck", dest="deck", help="Deck name", required=True, nargs=1
        )
        language = Language()
        self.parser.add_argument(
            "-l",
            "--language",
            dest="language_code",
            help="Language code",
            choices=language.get_language_codes(),
        )

    def parse_args(self):
        """Parse command line arguments."""
        return self.parser.parse_args()

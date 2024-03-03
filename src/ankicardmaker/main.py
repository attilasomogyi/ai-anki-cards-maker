# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Anki Card Maker main module."""

import sys
from multiprocessing import Process
from time import sleep
from mimetypes import guess_type
from pyperclip import waitForNewPaste
from ankicardmaker.commandline import CommandLine
from ankicardmaker.worker import Worker
from ankicardmaker.pdf import Pdf


class Main:
    """Anki Card Maker main class."""

    __slots__ = ("parser", "args", "deck_name", "language_code", "verbose", "worker")

    def __init__(self):
        """Initialize the AnkiCardMaker class."""
        self.args = CommandLine().get_parse_args()
        self.deck_name = self.args.deck_name[0]
        self.language_code = self.args.language_code[0]
        self.verbose = self.args.verbose
        self.worker = Worker(self.verbose)

    def print_verbose(self, section: str):
        """Print verbose."""
        if self.verbose:
            print(f"Deck name: {self.deck_name}")
            print(f"Processing section:\n{section}\n")

    def pdf_to_anki_cards(self):
        """Convert PDF to Anki cards."""
        if not (self.args.file_path) or (
            guess_type(self.args.file_path[0])[0] != "application/pdf"
        ):
            raise ValueError("File must be a PDF.")
        for page in Pdf(self.args.file_path[0]).get_pages_text():
            if page:
                try:
                    self.print_verbose(page)
                    Process(
                        target=self.worker.run,
                        args=(page, self.deck_name, self.language_code),
                    ).start()
                    rate_limit_per_minute = 3
                    sleep(60.0 / rate_limit_per_minute)
                except ValueError as error:
                    print(f"An error occurred: {error}")

    def clipboard_to_anki_cards(self):
        """Convert clipboard to Anki cards."""
        try:
            while True:
                clipboard = str(waitForNewPaste()).rstrip()
                self.print_verbose(clipboard)
                try:
                    Process(
                        target=self.worker.run,
                        args=(clipboard, self.deck_name, self.language_code),
                    ).start()
                except ValueError as error:
                    print(f"An error occurred: {error}")
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)

    def run(self):
        """Run the Anki Card Maker."""
        if self.args.file_path:
            self.pdf_to_anki_cards()
        else:
            self.clipboard_to_anki_cards()


def main():
    """Run the Anki Card Maker."""
    Main().run()


if __name__ == "__main__":
    main()

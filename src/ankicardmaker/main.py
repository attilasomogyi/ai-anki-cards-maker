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


# pylint: disable=too-few-public-methods
class Main:
    """Anki Card Maker main class."""

    __slots__ = (
        "__parser",
        "__args",
        "__deck_name",
        "__language_code",
        "__verbose",
        "__worker",
    )

    def __init__(self):
        """Initialize the AnkiCardMaker class."""
        self.__args = CommandLine().get_parse_args()
        self.__deck_name = self.__args.deck_name[0]
        self.__language_code = self.__args.language_code[0]
        self.__verbose = self.__args.verbose
        self.__worker = Worker(self.__verbose)

    def __print_verbose(self, section: str):
        """Print verbose."""
        if self.__verbose:
            print(f"Deck name: {self.__deck_name}")
            print(f"Processing section:\n{section}\n")

    def __pdf_to_anki_cards(self):
        """Convert PDF to Anki cards."""
        if not (self.__args.file_path) or (
            guess_type(self.__args.file_path[0])[0] != "application/pdf"
        ):
            raise ValueError("File must be a PDF.")
        for page in Pdf(self.__args.file_path[0]).get_pages_text():
            if page:
                try:
                    self.__print_verbose(page)
                    Process(
                        target=self.__worker.run,
                        args=(page, self.__deck_name, self.__language_code),
                    ).start()
                    rate_limit_per_minute = 3
                    sleep(60.0 / rate_limit_per_minute)
                except ValueError as error:
                    print(f"An error occurred: {error}")

    def __clipboard_to_anki_cards(self):
        """Convert clipboard to Anki cards."""
        try:
            while True:
                clipboard = str(waitForNewPaste()).rstrip()
                self.__print_verbose(clipboard)
                try:
                    Process(
                        target=self.__worker.run,
                        args=(clipboard, self.__deck_name, self.__language_code),
                    ).start()
                except ValueError as error:
                    print(f"An error occurred: {error}")
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)

    def run(self):
        """Run the Anki Card Maker."""
        if self.__args.file_path:
            self.__pdf_to_anki_cards()
        else:
            self.__clipboard_to_anki_cards()


def main():
    """Run the Anki Card Maker."""
    Main().run()


if __name__ == "__main__":
    main()

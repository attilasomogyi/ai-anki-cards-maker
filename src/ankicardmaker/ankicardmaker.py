"""Anki Card Maker module."""

import sys
from multiprocessing import Process
from time import sleep
from mimetypes import guess_type
from pyperclip import waitForNewPaste
from ankicardmaker.commandline import CommandLine
from ankicardmaker.worker import Worker
from ankicardmaker.pdf import Pdf


class AnkiCardMaker:
    """Main class for the Anki Card Maker."""

    def __init__(self):
        """Initialize the AnkiCardMaker class."""
        self.parser = CommandLine()
        self.args = self.parser.get_parse_args()
        self.deck_name = self.args.deck_name[0]
        self.language_code = self.args.language_code[0]
        self.worker = Worker()

    def pdf_to_anki_cards(self):
        """Convert PDF to Anki cards."""
        if not (self.args.file_path) or (
            guess_type(self.args.file_path[0])[0] != "application/pdf"
        ):
            raise ValueError("File must be a PDF.")
        for page in Pdf(self.args.file_path[0]).get_pages_text():
            if page:
                try:
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

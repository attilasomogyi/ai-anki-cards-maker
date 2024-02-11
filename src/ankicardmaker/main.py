"""Main module for the Anki Card Maker."""

import sys
from multiprocessing import Process
from time import sleep
from mimetypes import guess_type
from pyperclip import waitForNewPaste
from ankicardmaker.commandline import CommandLine
from ankicardmaker.worker import Worker
from ankicardmaker.pdf import Pdf


def main():
    """Main function."""
    parser = CommandLine()
    args = parser.get_parse_args()
    deck_name = args.deck_name[0]
    language_code = args.language_code[0]
    worker = Worker()
    if args.file_path:
        file_path = args.file_path[0]
        mime_type = guess_type(file_path)[0]
        if mime_type != "application/pdf":
            raise ValueError("File must be a PDF.")
        pdf = Pdf(args.file_path[0])
        pages = pdf.get_pages_text()
        for page in pages:
            print(page)
            if page != "":
                try:
                    process = Process(
                        target=worker.run, args=(page, deck_name, language_code)
                    )
                    process.start()
                except ValueError as error:
                    print(f"An error occurred: {error}")
                rate_limit_per_minute = 3
                delay = 60.0 / rate_limit_per_minute
                sleep(delay)

    else:
        try:
            while True:
                clipboard = str(waitForNewPaste()).rstrip()
                print(clipboard)
                try:
                    process = Process(
                        target=worker.run, args=(clipboard, deck_name, language_code)
                    )
                    process.start()
                except ValueError as error:
                    print(f"An error occurred: {error}")
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)


if __name__ == "__main__":
    main()

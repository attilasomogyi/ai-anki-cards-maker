"""Main module for the Anki Card Maker."""

from asyncio import run
import sys
from mimetypes import guess_type
from concurrent.futures import ThreadPoolExecutor
from pyperclip import waitForNewPaste
from ankicardmaker.commandline import CommandLine
from ankicardmaker.worker import worker
from ankicardmaker.pdf import Pdf


def main():
    """Main function."""
    parser = CommandLine()
    args = parser.get_parse_args()
    deck_name = args.deck_name[0]
    language_code = args.language_code[0]
    executor = ThreadPoolExecutor(max_workers=2)
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
                    executor.submit(run(worker(page, deck_name, language_code)))
                except ValueError as error:
                    print(f"An error occurred: {error}")
    else:
        try:
            while True:
                clipboard = str(waitForNewPaste()).rstrip()
                print(clipboard)
                try:
                    executor.submit(run(worker(clipboard, deck_name, language_code)))
                except ValueError as error:
                    print(f"An error occurred: {error}")
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)


if __name__ == "__main__":
    main()

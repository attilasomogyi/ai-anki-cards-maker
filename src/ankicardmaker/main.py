"""Main module for the Anki Card Maker."""

from asyncio import run
import sys
from pyperclip import waitForNewPaste
from ankicardmaker.commandline import CommandLine
from ankicardmaker.worker import worker


def main():
    """Main function."""
    parser = CommandLine()
    args = parser.get_parse_args()
    try:
        while True:
            clipboard = str(waitForNewPaste()).rstrip()
            deck_name = str(args.deck_name[0])
            language_code = str(args.language_code[0])
            print(clipboard)
            try:
                run(worker(clipboard, deck_name, language_code))
            except ValueError as error:
                print(f"An error occurred: {error}")
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()

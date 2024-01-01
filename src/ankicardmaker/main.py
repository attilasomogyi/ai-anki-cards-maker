"""Main module for the Anki Card Maker."""

from asyncio import run
import sys
from pyperclip import waitForNewPaste
from ankicardmaker.commandline import CommandLine
from ankicardmaker.worker import worker


def main():
    """Main function."""
    parser = CommandLine()
    args = parser.parse_args()
    try:
        while True:
            clipboard = str(waitForNewPaste()).rstrip()
            print(clipboard)
            run(worker(clipboard, args.deck, args.language_code))
    except KeyboardInterrupt:
        print("Exiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()

from ankicardmaker.commandline import CommandLine
from ankicardmaker.worker import worker
from pyperclip import paste, waitForNewPaste
from asyncio import run


def main():
    parser = CommandLine()
    args = parser.parse_args()
    try:
        while True:
            clipboard = str(waitForNewPaste()).rstrip()
            print(clipboard)
            run(worker(clipboard,args.deck,args.language_code))
    except KeyboardInterrupt:
            print("Exiting...")
            exit(0)

if __name__ == "__main__":
    main()

# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for converting clipboard to Anki cards."""

from multiprocessing import Process
import sys
from pyperclip import waitForNewPaste
from ankicardmaker.modules.main.verbose import MainVerbose
from ankicardmaker.modules.worker.run import WorkerRun


# pylint: disable=too-few-public-methods
class MainClipboardToAnkiCards:
    """Class providing a function to convert clipboard to Anki cards."""

    @staticmethod
    def convert(deck_name: str, language_code, verbose=False) -> None:
        """Convert clipboard to Anki cards."""
        try:
            while True:
                clipboard = str(waitForNewPaste()).rstrip()
                if verbose:
                    MainVerbose.print(deck_name, clipboard)
                try:
                    Process(
                        target=WorkerRun.run,
                        args=(clipboard, deck_name, language_code, verbose),
                    ).start()
                except ValueError as error:
                    print(f"An error occurred: {error}")
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit(0)

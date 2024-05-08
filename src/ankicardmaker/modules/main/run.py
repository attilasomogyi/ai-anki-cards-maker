# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for running the Anki Card Maker."""

from ankicardmaker.modules.command_line.parser_args import CommandLineParserArgs
from ankicardmaker.modules.main.clipboard_to_anki_cards import MainClipboardToAnkiCards
from ankicardmaker.modules.main.pdf_to_anki_cards import MainPdfToAnkiCards


# pylint: disable=too-few-public-methods
class MainRun:
    """Class providing a function to run the Anki Card Maker."""

    def run(self):
        """Run the Anki Card Maker."""
        args = CommandLineParserArgs.parse()
        if args.file_path:
            MainPdfToAnkiCards.convert(
                args.file_path,
                args.deck_name[0],
                args.language_code[0],
                args.verbose,
            )
        else:
            MainClipboardToAnkiCards.convert(
                args.deck_name[0],
                args.language_code[0],
                args.verbose,
            )

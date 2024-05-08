# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for converting PDF to Anki cards."""

from mimetypes import guess_type
from multiprocessing import Process
from time import sleep
from ankicardmaker.modules.main.verbose import MainVerbose
from ankicardmaker.modules.pdf.pages_text import PdfPagesText
from ankicardmaker.modules.worker.run import WorkerRun


# pylint: disable=too-few-public-methods
class MainPdfToAnkiCards:
    """Class providing a function to convert PDF to Anki cards."""

    @staticmethod
    def convert(
        file_path: str, deck_name: str, language_code: str, verbose=False
    ) -> None:
        """Convert PDF to Anki cards."""
        if not (file_path) or (guess_type(file_path[0])[0] != "application/pdf"):
            raise ValueError("File must be a PDF.")
        for page in PdfPagesText.get(file_path[0]):
            if page:
                try:
                    if verbose:
                        MainVerbose.print(deck_name, page)
                    Process(
                        target=WorkerRun.run,
                        args=(page, deck_name, language_code, verbose),
                    ).start()
                    rate_limit_per_minute = 3
                    sleep(60.0 / rate_limit_per_minute)
                except ValueError as error:
                    print(f"An error occurred: {error}")

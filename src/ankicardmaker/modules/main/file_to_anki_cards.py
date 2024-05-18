# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for converting PDF to Anki cards."""

from mimetypes import guess_type
from pathlib import Path
from multiprocessing import Process
from time import sleep
from rich.progress import track
from ankicardmaker.modules.main.verbose import MainVerbose
from ankicardmaker.modules.pdf.pages_text import PdfPagesText
from ankicardmaker.modules.pptx.pages_text import PptxPagesText
from ankicardmaker.modules.worker.run import WorkerRun


# pylint: disable=too-few-public-methods
class MainFileToAnkiCards:
    """Class providing a function to convert PDF to Anki cards."""

    @staticmethod
    def convert(
        file_path: Path, deck_name: str, language_code: str, verbose=False
    ) -> None:
        """Convert PDF to Anki cards."""
        file_type = guess_type(file_path)[0]
        file_types = [
            "application/pdf",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "application/vnd.ms-powerpoint",
        ]
        if not (file_path) or file_type not in file_types:
            raise ValueError("File must be a PDF or PPT or PPTX.")
        if file_type == "application/pdf":
            pages = PdfPagesText.get(file_path)
        else:
            pages = PptxPagesText.get(file_path)
        for page in track(pages, description="Processing file"):
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

# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""The module to handle the pdf file"""

from pathlib import Path
import fitz


# pylint: disable=too-few-public-methods
class Pdf:
    """Class providing a function to handle the pdf file"""

    __slots__ = ("__pdf_file_path", "__doc")

    def __init__(self, pdf_file_path: Path):
        self.__pdf_file_path = pdf_file_path
        self.__doc = self.__open_pdf_file()

    def __open_pdf_file(self) -> fitz.Document:
        """Open the pdf file"""
        return fitz.open(self.__pdf_file_path)

    def get_pages_text(self) -> list[str]:
        """Get the text of the pages"""
        pages = []
        for page in self.__doc:
            text = page.get_text("text")
            if text:
                text = text.replace("\n", " ").replace(r"\s{2,}", " ")
                pages.append(text)
        return pages

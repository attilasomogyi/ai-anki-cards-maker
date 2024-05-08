# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling pdf pages text."""

from ankicardmaker.modules.pdf.file import PdfFile


# pylint: disable=too-few-public-methods
class PdfPagesText:
    """Class providing a function to get the text of the pages"""

    @staticmethod
    def get(pdf_file_path) -> list[str]:
        """Get the text of the pages"""
        pages = []
        for page in PdfFile().open(pdf_file_path):
            text = page.get_text("text")
            if text:
                text = text.replace("\n", " ").replace(r"\s{2,}", " ")
                pages.append(text)
        return pages

# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling the pdf file."""

import fitz


# pylint: disable=too-few-public-methods
class PdfFile:
    """Class providing a function to handle the pdf file"""

    @staticmethod
    def open(pdf_file_path):
        """Open the pdf file"""
        return fitz.open(pdf_file_path)

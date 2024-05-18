# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling the pptx file."""

from pptx import Presentation


# pylint: disable=too-few-public-methods
class PptxFile:
    """Class providing a function to handle the pptx file"""

    @staticmethod
    def open(pptx_file_path):
        """Open the pptx file"""
        return Presentation(pptx_file_path)

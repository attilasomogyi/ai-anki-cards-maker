# SPDX-FileCopyrightText: Copyright 2023-2024 Attila Zsolt Somogyi
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Module for handling pptx pages text."""

from ankicardmaker.modules.pptx.file import PptxFile


# pylint: disable=too-few-public-methods
class PptxPagesText:
    """Class providing a function to get the text of the pages"""

    @staticmethod
    def get(pptx_file_path) -> list[str]:
        """Get the text of the pages"""
        pages = []
        for slide in PptxFile().open(pptx_file_path).slides:
            text = ""
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text += shape.text
            if text:
                text = text.replace("\n", " ").replace(r"\s{2,}", " ")
                pages.append(text)
        return pages

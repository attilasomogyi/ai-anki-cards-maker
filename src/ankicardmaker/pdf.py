"""The module to handle the pdf file"""

import fitz


class Pdf:
    """Class providing a function to handle the pdf file"""

    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path
        self.doc = self.open_pdf_file(self.pdf_file_path)

    def open_pdf_file(self, pdf_file_path):
        """Open the pdf file"""
        return fitz.open(pdf_file_path)

    def get_pages_text(self):
        """Get the text of the pages"""
        pages = []
        for page in self.doc:
            text = page.get_text("text")
            if text:
                text = text.replace("\n", " ").replace(r"\s{2,}", " ")
                pages.append(text)
        return pages

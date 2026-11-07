import os

from pypdf import PdfWriter

from src.pdf_utils import save_pdf


class PDFSplitter:
    """Splits a PDF into single pages, or extracts selected pages."""

    def __init__(self, split_folder="output/split", extract_folder="output/extracted"):
        self.split_folder = split_folder
        self.extract_folder = extract_folder

    def split_pdf(self, document):
        reader = document.open_pdf()
        base_name = os.path.splitext(document.file_name)[0]
        saved_files = []
        for number, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()                 # a NEW writer for every page
            writer.add_page(page)
            saved_files.append(
                save_pdf(writer, self.split_folder, f"{base_name}_page_{number}.pdf")
            )
        return saved_files

    def extract_pages(self, document, page_numbers, output_name=None):
        reader = document.open_pdf()
        total_pages = len(reader.pages)

        if not page_numbers:
            raise ValueError("No page numbers given")
        for number in page_numbers:              # validate BEFORE extracting
            if not 1 <= number <= total_pages:
                raise ValueError(
                    f"Invalid page number {number}. This PDF has {total_pages} page(s)"
                )

        writer = PdfWriter()
        for number in page_numbers:
            writer.add_page(reader.pages[number - 1])      # user pages start at 1, index at 0

        if output_name is None:
            base_name = os.path.splitext(document.file_name)[0]
            output_name = f"{base_name}_extracted.pdf"
        return save_pdf(writer, self.extract_folder, output_name)

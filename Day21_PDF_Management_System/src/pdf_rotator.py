import os

from pypdf import PdfWriter

from src.pdf_utils import save_pdf

VALID_ANGLES = (90, 180, 270)


class PDFRotator:
    """Rotates one page of a PDF and saves the result as a NEW file."""

    def __init__(self, output_folder="output/rotated"):
        self.output_folder = output_folder

    def rotate_pdf(self, document, page_number, angle, output_name=None):
        if angle not in VALID_ANGLES:
            raise ValueError("Rotation angle must be 90, 180 or 270")

        reader = document.open_pdf()
        total_pages = len(reader.pages)
        if not 1 <= page_number <= total_pages:
            raise ValueError(
                f"Invalid page number {page_number}. This PDF has {total_pages} page(s)"
            )

        writer = PdfWriter()
        for number, page in enumerate(reader.pages, start=1):
            if number == page_number:
                page.rotate(angle)               # clockwise
            writer.add_page(page)                # keep ALL pages in the new file

        if output_name is None:
            base_name = os.path.splitext(document.file_name)[0]
            output_name = f"{base_name}_rotated.pdf"
        return save_pdf(writer, self.output_folder, output_name)

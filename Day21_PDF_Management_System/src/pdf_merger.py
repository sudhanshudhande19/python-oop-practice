from pypdf import PdfWriter

from src.pdf_utils import save_pdf


class PDFMerger:
    """Merges several PDFDocument objects into one PDF (composition: it USES PDFDocument)."""

    def __init__(self, output_folder="output/merged"):
        self.output_folder = output_folder

    def merge_pdfs(self, documents, output_name="merged.pdf"):
        if len(documents) < 2:
            raise ValueError("Select at least two PDF files to merge")
        if not output_name.lower().endswith(".pdf"):
            output_name += ".pdf"

        writer = PdfWriter()
        for document in documents:               # the order of the list = the order of the pages
            writer.append(document.open_pdf())
        return save_pdf(writer, self.output_folder, output_name)

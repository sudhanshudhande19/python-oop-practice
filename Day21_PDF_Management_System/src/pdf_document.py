import os

from pypdf import PdfReader
from pypdf.errors import PdfReadError

from src.pdf_utils import format_size


class PDFDocument:
    """One PDF file: validates the path, opens it, counts pages, gives information."""

    def __init__(self, file_path):
        if file_path is None or not str(file_path).strip():
            raise ValueError("File path cannot be empty")

        file_path = str(file_path).strip().strip('"')      # allow "Copy as path" quotes
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        if not os.path.isfile(file_path):
            raise ValueError(f"This is a folder, not a file: {file_path}")
        if not file_path.lower().endswith(".pdf"):
            raise ValueError("Only .pdf files are supported")

        self.__file_path = file_path                        # encapsulated (private)
        self.file_name = os.path.basename(file_path)

    @property
    def file_path(self):                                    # read-only access
        return self.__file_path

    def open_pdf(self):
        """Return a PdfReader. Converts pypdf errors into clear ValueErrors."""
        try:
            reader = PdfReader(self.__file_path)
            if reader.is_encrypted and reader.decrypt("") == 0:
                raise ValueError(f"PDF is password protected: {self.file_name}")
            len(reader.pages)                               # forces pypdf to read the pages
            return reader
        except PdfReadError:
            raise ValueError(f"Invalid or corrupted PDF file: {self.file_name}") from None

    def count_pages(self):
        return len(self.open_pdf().pages)

    def get_information(self):
        """Return a dictionary with the basic information of the PDF."""
        reader = self.open_pdf()
        meta = reader.metadata                              # can be None
        return {
            "File name": self.file_name,
            "Total pages": len(reader.pages),
            "File size": format_size(os.path.getsize(self.__file_path)),
            "Title": (meta.title if meta and meta.title else "Not available"),
            "Author": (meta.author if meta and meta.author else "Not available"),
            "Creator": (meta.creator if meta and meta.creator else "Not available"),
        }

    @classmethod
    def create_from_text(cls, text, output_path):
        """Alternative constructor: build a NEW PDF from text, return a PDFDocument.

        pypdf cannot draw text, so this uses the reportlab library.
        """
        if text is None or not text.strip():
            raise ValueError("Text cannot be empty")
        if not output_path.lower().endswith(".pdf"):
            output_path += ".pdf"
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfgen import canvas
        except ImportError:
            raise RuntimeError("Creating PDFs needs reportlab. Run: pip install reportlab") from None

        folder = os.path.dirname(output_path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        pdf = canvas.Canvas(output_path, pagesize=A4)
        _, height = A4
        y = height - 50
        for line in text.splitlines():
            if y < 50:                                      # page is full → start a new page
                pdf.showPage()
                y = height - 50
            pdf.drawString(50, y, line)
            y -= 20
        pdf.save()
        return cls(output_path)

    def __str__(self):
        return f"PDFDocument({self.file_name})"

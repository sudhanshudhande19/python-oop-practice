"""Creates small sample PDFs inside the data/ folder (needs reportlab)."""

import os

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def make_pdf(path, title, pages):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    pdf = canvas.Canvas(path, pagesize=A4)
    pdf.setTitle(title)
    pdf.setAuthor("Test Author")
    for number in range(1, pages + 1):
        pdf.setFont("Helvetica-Bold", 28)
        pdf.drawString(80, 760, f"{title} - Page {number}")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(80, 720, "Sample page for testing the PDF Management System.")
        pdf.showPage()
    pdf.save()


if __name__ == "__main__":
    make_pdf("data/sample.pdf", "Sample", 3)
    make_pdf("data/other.pdf", "Other", 2)
    print("Sample PDFs created in the data/ folder")

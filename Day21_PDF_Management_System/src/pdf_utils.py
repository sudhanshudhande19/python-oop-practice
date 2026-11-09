"""Small helper functions shared by the PDF classes."""

import os


def save_pdf(writer, folder, file_name):
    """Save a PdfWriter into folder/file_name (binary mode) and return the path."""
    os.makedirs(folder, exist_ok=True)          # create the output folder if needed
    output_path = os.path.join(folder, file_name)
    with open(output_path, "wb") as file:       # "wb" = write binary (required for PDFs)
        writer.write(file)
    return output_path


def parse_page_numbers(text):
    """Convert '1,3,5' or '2-4,7' into a list of ints, e.g. [2, 3, 4, 7].

    Only checks the SYNTAX. The page range is validated by the PDF classes.
    """
    if text is None or not text.strip():
        raise ValueError("Page numbers cannot be empty")

    numbers = []
    for part in text.split(","):
        part = part.strip()
        try:
            if "-" in part:                      # a range such as 2-4
                start, end = part.split("-", 1)
                start, end = int(start), int(end)
                if start > end:
                    raise ValueError
                numbers.extend(range(start, end + 1))
            else:
                numbers.append(int(part))
        except ValueError:
            raise ValueError(f"Invalid page input: '{part}'") from None
    return numbers


def format_size(size_in_bytes):
    """Return a readable file size, e.g. '2.31 KB'."""
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    if size_in_bytes < 1024 * 1024:
        return f"{size_in_bytes / 1024:.2f} KB"
    return f"{size_in_bytes / (1024 * 1024):.2f} MB"

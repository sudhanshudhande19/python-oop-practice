import os

from src.pdf_document import PDFDocument
from src.pdf_merger import PDFMerger
from src.pdf_rotator import PDFRotator
from src.pdf_splitter import PDFSplitter
from src.pdf_utils import parse_page_numbers


class PDFManager:
    """Menu and application control. The ONLY class that uses input() and print()."""

    def __init__(self):
        self.merger = PDFMerger()                # has-a (composition)
        self.splitter = PDFSplitter()
        self.rotator = PDFRotator()

    def display_menu(self):
        print("\n=================================")
        print("       PDF MANAGEMENT SYSTEM")
        print("=================================\n")
        print("1. Create PDF")
        print("2. Merge PDFs")
        print("3. Split PDF")
        print("4. Extract Pages")
        print("5. Rotate PDF")
        print("6. Count PDF Pages")
        print("7. Display PDF Information")
        print("8. Exit\n")

    @staticmethod
    def ask_int(prompt):
        try:
            return int(input(prompt))
        except ValueError:
            raise ValueError("Please enter a whole number") from None

    def handle_choice(self, choice):
        """Run the selected option. Return False only when the user chooses Exit."""
        if choice == "1":
            file_name = os.path.basename(input("Output file name (e.g. notes.pdf): ").strip())
            if not file_name:
                raise ValueError("File name cannot be empty")
            print("Type your text. Press Enter on an empty line to finish:")
            lines = []
            while True:
                line = input()
                if not line:
                    break
                lines.append(line)
            document = PDFDocument.create_from_text(
                "\n".join(lines), os.path.join("output", "created", file_name)
            )
            print("PDF created:", document.file_path)

        elif choice == "2":
            paths = input("Enter PDF paths separated by commas: ").split(",")
            documents = [PDFDocument(path) for path in paths]
            print("Merged PDF saved:", self.merger.merge_pdfs(documents))

        elif choice == "3":
            document = PDFDocument(input("Enter PDF path: "))
            files = self.splitter.split_pdf(document)
            print(f"Split into {len(files)} file(s) in: {self.splitter.split_folder}")

        elif choice == "4":
            document = PDFDocument(input("Enter PDF path: "))
            print("Total pages:", document.count_pages())
            numbers = parse_page_numbers(input("Pages to extract (e.g. 1,3 or 2-4): "))
            print("Extracted PDF saved:", self.splitter.extract_pages(document, numbers))

        elif choice == "5":
            document = PDFDocument(input("Enter PDF path: "))
            print("Total pages:", document.count_pages())
            page_number = self.ask_int("Page number to rotate: ")
            angle = self.ask_int("Rotation angle (90, 180 or 270): ")
            print("Rotated PDF saved:", self.rotator.rotate_pdf(document, page_number, angle))

        elif choice == "6":
            document = PDFDocument(input("Enter PDF path: "))
            print("Total pages:", document.count_pages())

        elif choice == "7":
            document = PDFDocument(input("Enter PDF path: "))
            for label, value in document.get_information().items():
                print(f"{label}: {value}")

        elif choice == "8":
            print("Goodbye!")
            return False

        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
        return True

    def run(self):
        running = True
        while running:
            self.display_menu()
            try:
                choice = input("Enter your choice: ").strip()
                running = self.handle_choice(choice)
            except (ValueError, FileNotFoundError, PermissionError, RuntimeError) as error:
                print("Error:", error)             # the ONE place that reports errors
            except (KeyboardInterrupt, EOFError):
                print("\nGoodbye!")
                running = False

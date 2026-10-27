
from pathlib import Path
import shutil


class FileOrganizer:

    def __init__(self, directory_path):
        self.directory_path = Path(directory_path)

        self.file_categories = {
            "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
            "Documents": {
                ".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"
            },
            "Videos": {".mp4", ".mkv", ".mov", ".avi"},
            "Audio": {".mp3", ".wav", ".aac", ".flac"},
            "Code": {".py", ".js", ".html", ".css", ".java", ".cpp"},
            "Archives": {".zip", ".rar", ".7z", ".tar"},
            "Others": set()
        }

        self.files_moved = 0
        self.files_skipped = 0
        self.files_failed = 0
        self.failed_files = []
        self.scanned_files = []

    def validate_directory(self):
        """Check whether the source directory is valid."""
        try:
            if not self.directory_path.exists():
                print("Error: Directory does not exist.")
                return False

            if not self.directory_path.is_dir():
                print("Error: Path is not a directory.")
                return False

            return True

        except OSError as error:
            print(f"Directory access error: {error}")
            return False

    def scan_files(self):
        """Scan files in the source directory only."""
        if not self.validate_directory():
            return []

        try:
            self.scanned_files = [
                path for path in self.directory_path.iterdir()
                if path.is_file()
            ]

            print(f"\nFiles found: {len(self.scanned_files)}")

            for file in self.scanned_files:
                print(f"- {file.name}")

            return self.scanned_files

        except OSError as error:
            print(f"Scan failed: {error}")
            return []

    def create_folders(self):
        """Create category folders when needed."""
        try:
            for category in self.file_categories:
                folder = self.directory_path / category
                folder.mkdir(exist_ok=True)

            print("Category folders are ready.")
            return True

        except OSError as error:
            print(f"Folder creation failed: {error}")
            return False

    def get_category(self, file_path):
        """Return category based on file extension."""
        extension = Path(file_path).suffix.lower()

        for category, extensions in self.file_categories.items():
            if extension in extensions:
                return category

        return "Others"

    def get_unique_path(self, destination):
        """Choose a filename without overwriting existing files."""
        destination = Path(destination)

        if not destination.exists():
            return destination

        counter = 1

        while True:
            new_name = (
                f"{destination.stem}_{counter}"
                f"{destination.suffix}"
            )
            new_path = destination.with_name(new_name)

            if not new_path.exists():
                return new_path

            counter += 1

    def move_file(self, file_path, category):
        """Move one file safely into its category folder."""
        file_path = Path(file_path)

        try:
            if not file_path.is_file():
                self.files_skipped += 1
                print(f"Skipped: {file_path.name}")
                return

            destination_folder = self.directory_path / category
            destination_folder.mkdir(exist_ok=True)

            destination = self.get_unique_path(
                destination_folder / file_path.name
            )

            shutil.move(str(file_path), str(destination))

            self.files_moved += 1
            print(f"Moved: {file_path.name} -> {category}/{destination.name}")

        except (OSError, shutil.Error) as error:
            self.files_failed += 1
            self.failed_files.append((file_path.name, str(error)))
            print(f"Failed: {file_path.name} - {error}")

    def organize_files(self):
        """Organize all files found during scanning."""
        if not self.validate_directory():
            return

        files = self.scan_files()

        if not self.create_folders():
            return

        for file_path in files:
            category = self.get_category(file_path)
            self.move_file(file_path, category)

        print("\nOrganization process finished.")

    def preview_movements(self):
        """Show planned operations without moving files."""
        if not self.validate_directory():
            return

        try:
            files = [
                path for path in self.directory_path.iterdir()
                if path.is_file()
            ]

            if not files:
                print("No files to preview.")
                return

            print("\n--- Movement Preview (Dry Run) ---")

            for file_path in files:
                category = self.get_category(file_path)
                destination = self.directory_path / category
                planned_path = self.get_unique_path(
                    destination / file_path.name
                )

                print(
                    f"{file_path.name} -> "
                    f"{category}/{planned_path.name}"
                )

            print("Preview complete. No files were moved.")

        except OSError as error:
            print(f"Preview failed: {error}")

    def display_summary(self):
        """Display counts of successful and failed operations."""
        print("\n===== FILE ORGANIZER SUMMARY =====")
        print(f"Files moved   : {self.files_moved}")
        print(f"Files skipped : {self.files_skipped}")
        print(f"Files failed  : {self.files_failed}")

        if self.failed_files:
            print("\nFailed files:")
            for filename, reason in self.failed_files:
                print(f"- {filename}: {reason}")

        print("==================================")


def main():
    print("===== PYTHON FILE ORGANIZER =====")

    directory = input("Enter directory path: ").strip().strip('"')
    organizer = FileOrganizer(directory)

    if not organizer.validate_directory():
        return

    while True:
        print("""
1. Scan Directory
2. Preview File Movements
3. Organize Files
4. Display Summary
5. Exit
""")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            organizer.scan_files()

        elif choice == "2":
            organizer.preview_movements()

        elif choice == "3":
            confirm = input(
                "Move files for real? Type YES to continue: "
            ).strip()

            if confirm == "YES":
                organizer.organize_files()
            else:
                print("Organization cancelled.")

        elif choice == "4":
            organizer.display_summary()

        elif choice == "5":
            print("Exiting File Organizer. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()

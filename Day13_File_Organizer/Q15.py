# Improve your FileOrganizer class.

# Requirements:

    # Validate the source directory.
    # Handle permission errors.
    # Handle file movement errors.
    # Prevent duplicate filenames from being overwritten.
    # Display a summary of successful and failed operations.


#---------------------------------------------------------------------------------


from pathlib import Path
import shutil


class FileOrganizer:

    def __init__(self, directory):
        self.directory = Path(directory)

        self.categories = {
            "Images": {".jpg", ".jpeg", ".png", ".gif"},
            "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx"},
            "Videos": {".mp4", ".mkv", ".avi", ".mov"},
            "Audio": {".mp3", ".wav", ".aac", ".flac"},
        }

        self.successful = 0
        self.failed = 0
        self.errors = []

    def validate_directory(self):
        """Validate the source directory."""
        try:
            if not self.directory.exists():
                print("Error: Directory does not exist.")
                return False

            if not self.directory.is_dir():
                print("Error: The path is not a directory.")
                return False

            # Check whether directory can be accessed
            with self.directory.iterdir() as iterator:
                next(iterator, None)

            return True

        except (OSError, PermissionError) as error:
            print(f"Directory access error: {error}")
            return False

    def scan_files(self):
        """Scan source files safely."""
        try:
            files = [
                file for file in self.directory.iterdir()
                if file.is_file()
            ]
            print(f"Found {len(files)} files.")
            return files

        except OSError as error:
            print(f"Could not scan directory: {error}")
            return []

    def create_folders(self):
        """Create category folders."""
        try:
            for folder in list(self.categories) + ["Others"]:
                (self.directory / folder).mkdir(
                    parents=True, exist_ok=True
                )

            return True

        except OSError as error:
            print(f"Could not create folders: {error}")
            return False

    def get_category(self, file):
        """Identify the file category."""
        extension = file.suffix.lower()

        for category, extensions in self.categories.items():
            if extension in extensions:
                return category

        return "Others"

    def get_unique_path(self, destination):
        """Generate a unique filename without overwriting."""
        if not destination.exists():
            return destination

        folder = destination.parent
        stem = destination.stem
        suffix = destination.suffix
        counter = 1

        while True:
            new_path = folder / f"{stem}_{counter}{suffix}"

            if not new_path.exists():
                return new_path

            counter += 1

    def organize_files(self, files):
        """Move files and record operation results."""
        for file in files:
            try:
                category = self.get_category(file)
                destination_folder = self.directory / category

                # Skip files already inside a category folder
                if file.parent == destination_folder:
                    continue

                destination_folder.mkdir(
                    parents=True, exist_ok=True
                )

                destination = self.get_unique_path(
                    destination_folder / file.name
                )

                shutil.move(str(file), str(destination))

                self.successful += 1
                print(f"SUCCESS: {file.name} -> {destination.name}")

            except (OSError, shutil.Error) as error:
                self.failed += 1
                self.errors.append((file.name, str(error)))
                print(f"FAILED: {file.name} - {error}")

    def display_summary(self):
        """Display successful and failed operations."""
        print("\n===== ORGANIZATION SUMMARY =====")
        print(f"Successful operations: {self.successful}")
        print(f"Failed operations: {self.failed}")

        if self.errors:
            print("\nFailed files:")
            for filename, error in self.errors:
                print(f"- {filename}: {error}")

        print("================================")


# Run the program
organizer = FileOrganizer("MyFiles")

if organizer.validate_directory():
    files = organizer.scan_files()

    if organizer.create_folders():
        organizer.organize_files(files)

    organizer.display_summary()

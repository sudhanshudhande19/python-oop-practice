# reate a class named FileOrganizer.

# Requirements:

    # Accept a directory path in the constructor.
    # Create a method scan_files().
    # Create a method create_folders().
    # Create a method organize_files().
    # Create a method display_summary().
    # Use separate methods for separate responsibilities.

#--------------------------------------------------------------------------------------------------------------


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

        self.files = []
        self.summary = {}

    def scan_files(self):
        """Find files in the specified directory."""
        if not self.directory.is_dir():
            print("Directory does not exist.")
            return

        self.files = [
            file for file in self.directory.iterdir()
            if file.is_file()
        ]

        print(f"Found {len(self.files)} files.")

    def create_folders(self):
        """Create category folders if needed."""
        for folder in list(self.categories) + ["Others"]:
            folder_path = self.directory / folder
            folder_path.mkdir(parents=True, exist_ok=True)

        print("Category folders are ready.")

    def get_category(self, file):
        """Identify the category of a file."""
        extension = file.suffix.lower()

        for category, extensions in self.categories.items():
            if extension in extensions:
                return category

        return "Others"

    def organize_files(self):
        """Move files into their respective folders."""
        self.summary = {category: 0 for category in self.categories}
        self.summary["Others"] = 0

        for file in self.files:
            category = self.get_category(file)
            destination_folder = self.directory / category
            destination = destination_folder / file.name

            # Avoid overwriting existing files
            counter = 1
            while destination.exists():
                destination = destination_folder / (
                    f"{file.stem}_{counter}{file.suffix}"
                )
                counter += 1

            try:
                shutil.move(str(file), str(destination))
                self.summary[category] += 1
                print(f"Moved: {file.name} -> {category}/")

            except OSError as error:
                print(f"Could not move {file.name}: {error}")

    def display_summary(self):
        """Display the number of files organized."""
        print("\n--- Organization Summary ---")

        for category, count in self.summary.items():
            print(f"{category}: {count} files")

        print("Organization completed!")


# Create an object
organizer = FileOrganizer("MyFiles")

# Call the methods
organizer.scan_files()
organizer.create_folders()
organizer.organize_files()
organizer.display_summary()

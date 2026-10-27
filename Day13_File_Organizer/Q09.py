# Write a program that moves unrecognized file types into an Others folder.

# Requirements:

    # Do not move folders.
    # Do not move the organizer's own Python script.
    # Keep the program from crashing when a file operation fails.

#-------------------------------------------------------------------------------------------------------------


from pathlib import Path
import shutil

# Directory to organize
directory = Path("MyFiles")
directory.mkdir(parents=True, exist_ok=True)

# Recognized extensions
known_extensions = {
    # Images
    ".jpg", ".jpeg", ".png", ".gif", ".webp",
    # Documents
    ".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx",
    # Videos
    ".mp4", ".mkv", ".avi", ".mov", ".wmv",
    # Audio
    ".mp3", ".wav", ".aac", ".flac", ".ogg"
}

# Organizer script path
script_path = Path(__file__).resolve()

# Create Others folder
others_folder = directory / "Others"
others_folder.mkdir(exist_ok=True)

# Move unrecognized files
for file in directory.iterdir():

    # Ignore folders
    if not file.is_file():
        continue

    # Ignore the organizer's own script
    if file.resolve() == script_path:
        continue

    # Ignore recognized file types
    if file.suffix.lower() in known_extensions:
        continue

    # Move unrecognized files safely
    try:
        destination = others_folder / file.name
        shutil.move(str(file), str(destination))
        print(f"Moved to Others: {file.name}")

    except OSError as error:
        print(f"Could not move {file.name}: {error}")

print("File organization completed!")


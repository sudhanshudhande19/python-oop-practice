# Create a program that previews file movements without actually moving any files.

# Example:
    # photo.jpg  -> Images/
    # report.pdf -> Documents/
    # movie.mp4  -> Videos/

# Requirements:

    # Display the planned operations.
    # Do not modify files in dry-run mode.
    # Allow actual movement when dry-run mode is disabled.

#--------------------------------------------------------------------------------------------------------------------------------


from pathlib import Path
import shutil

def organize_files(directory, dry_run=True):
    directory = Path(directory)

    categories = {
        "Images": {".jpg", ".jpeg", ".png", ".gif"},
        "Documents": {".pdf", ".docx", ".doc", ".txt", ".xlsx"},
        "Videos": {".mp4", ".mkv", ".avi", ".mov"},
        "Audio": {".mp3", ".wav", ".aac", ".flac"}
    }

    for file in directory.iterdir():

        if not file.is_file():
            continue

        # Identify the category
        category = "Others"

        for folder, extensions in categories.items():
            if file.suffix.lower() in extensions:
                category = folder
                break

        destination_folder = directory / category
        destination = destination_folder / file.name

        # Display planned operation
        print(f"{file.name} -> {category}/")

        if not dry_run:
            try:
                destination_folder.mkdir(exist_ok=True)

                # Avoid overwriting existing files
                counter = 1
                while destination.exists():
                    destination = destination_folder / (
                        f"{file.stem}_{counter}{file.suffix}"
                    )
                    counter += 1

                shutil.move(str(file), str(destination))
                print(f"Moved to: {destination.name}")

            except OSError as error:
                print(f"Could not move {file.name}: {error}")

    if dry_run:
        print("\nDry run completed. No files were moved.")
    else:
        print("\nFile organization completed!")


# True = Preview only
# False = Actually move files
organize_files("MyFiles", dry_run=True)

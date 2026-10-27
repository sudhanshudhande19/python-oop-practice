# Write a program that handles two files with the same name in a destination folder.

# Requirements:

    # Never overwrite an existing file.
    # Rename the incoming file, for example photo_1.jpg.
    # Generate another unique name if that name also exists

#-------------------------------------------------------------------------------------------------------------------


from pathlib import Path
import shutil

def get_unique_path(destination):
    destination = Path(destination)

    # If the filename already exists
    if not destination.exists():
        return destination

    folder = destination.parent
    stem = destination.stem
    suffix = destination.suffix

    counter = 1

    while True:
        new_name = f"{stem}_{counter}{suffix}"
        new_path = folder / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def move_file(source, destination_folder):
    source = Path(source)
    destination_folder = Path(destination_folder)

    destination_folder.mkdir(parents=True, exist_ok=True)

    destination = destination_folder / source.name
    unique_destination = get_unique_path(destination)

    try:
        shutil.move(str(source), str(unique_destination))
        print(f"Moved: {source.name} -> {unique_destination.name}")

    except OSError as error:
        print(f"Could not move {source.name}: {error}")


# Example usage
move_file("photo.jpg", "Images")

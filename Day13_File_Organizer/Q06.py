# Write a program that moves image files into an Images folder.

# Requirements:
    # Support .jpg, .jpeg, .png, and .gif.
    # Create the destination folder if it does not exist.
    # Test with sample files.

#--------------------------------------------------------------------------------------------


from pathlib import Path
import shutil

# Main directory
directory = Path("MyFiles")

# Create sample files for testing
directory.mkdir(parents=True, exist_ok=True)

sample_files = [
    "photo.jpg",
    "image.jpeg",
    "logo.png",
    "animation.gif",
    "notes.txt"
]

for filename in sample_files:
    file_path = directory / filename
    if not file_path.exists():
        file_path.write_text("Sample file for testing")

# Create Images folder
images_folder = directory / "Images"
images_folder.mkdir(exist_ok=True)

# Supported image extensions
image_extensions = {".jpg", ".jpeg", ".png", ".gif"}

# Move image files
for file in directory.iterdir():
    if file.is_file() and file.suffix.lower() in image_extensions:
        shutil.move(str(file), str(images_folder / file.name))
        print(f"Moved: {file.name}")

print("Image files organized successfully!")

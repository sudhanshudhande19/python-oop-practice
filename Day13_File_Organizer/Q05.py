# Create a dictionary that maps file extensions to categories.

# Example:

    # .jpg, .png, .jpeg → Images
    # .pdf, .docx, .txt → Documents
    # .mp4, .mkv → Videos
    # .mp3, .wav → Audio
    # Add at least five more extensions of your choice.


#---------------------------------------------------------------------------------------------


extension_categories = {
    # Images
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",

    # Documents
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".doc": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",

    # Videos
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",

    # Programming files
    ".py": "Others",
    ".java": "Others",
    ".cpp": "Others"
}

print(extension_categories)

extension = ".jpg"
category = extension_categories.get(extension, "Others")
print(category)

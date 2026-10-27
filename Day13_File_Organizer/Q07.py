# Write a program that moves document files into a Documents folder.

# Requirements:

    # Support .pdf, .docx, .doc, .txt, and .xlsx.

    # Ignore files belonging to other categories.\

#-----------------------------------------------------------------------------------------------


from pathlib import Path
import shutil

# Specify the directory
directory = Path("MyFiles")

# Create directory if it does not exist
directory.mkdir(parents=True, exist_ok=True)

# Supported document extensions
document_extensions = {".pdf", ".docx", ".doc", ".txt", ".xlsx"}

# Create Documents folder
documents_folder = directory / "Documents"
documents_folder.mkdir(exist_ok=True)

# Move only document files
for file in directory.iterdir():
    if file.is_file() and file.suffix.lower() in document_extensions:
        shutil.move(str(file), str(documents_folder / file.name))
        print(f"Moved: {file.name}")

print("Document files organized successfully!")

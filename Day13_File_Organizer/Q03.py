# Write a program that displays the extensions of files in a directory.

# Example extensions:

    # .jpg
    # .pdf
    # .py
    # .txt

# Display each filename with its extension.

#-----------------------------------------------------------------------------------------------



from pathlib import Path

folder_path = Path(".")

for file in folder_path.iterdir():
    if file.is_file():
        print(f"{file.name} - {file.suffix}")

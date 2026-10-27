# Write a program that displays the size of each file in a directory.

# Requirements:

    # Display sizes in bytes.
    # Calculate the total size of all files.
    # Handle inaccessible files gracefully

#-----------------------------------------------------------------------------------------------------


from pathlib import Path

# Specify the directory
directory = Path("MyFiles")

total_size = 0

for file in directory.iterdir():

    if file.is_file():
        try:
            size = file.stat().st_size
            print(f"{file.name} : {size} bytes")

            total_size += size

        except OSError as error:
            print(f"Cannot access {file.name}: {error}")

print(f"\nTotal size of all accessible files: {total_size} bytes")

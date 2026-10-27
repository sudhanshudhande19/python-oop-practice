# Write a program that counts how many files belong to each extension.

# Example output:
    # .jpg : 5 files
    # .pdf : 3 files
    # .py  : 4 files
    # .txt : 2 files

# Requirements:

    # Handle uppercase extensions such as .JPG.
    # Ignore files without extensions or count them under No Extension.

#--------------------------------------------------------------------------------------------------------------


from pathlib import Path
from collections import Counter

# Specify the directory
directory = Path("MyFiles")

# Store extension counts
extension_counts = Counter()

# Count files
for file in directory.iterdir():

    if file.is_file():
        extension = file.suffix.lower()

        if extension:
            extension_counts[extension] += 1
        else:
            extension_counts["No Extension"] += 1

# Display results
for extension, count in sorted(extension_counts.items()):
    print(f"{extension} : {count} files")

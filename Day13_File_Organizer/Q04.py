# Write a program that creates these folders inside a specified directory:

    # - Images
    # - Documents
    # - Videos
    # - Audio
    # - Others

# Requirements:

    # - Create folders only when needed.
    # - Do not raise an error if a folder already exists.

#----------------------------------------------------------------------------------------------------------


from pathlib import Path

directory = Path("MyFiles")

folders = ["Images", "Documents", "Videos", "Audio", "Others"]

for folder in folders:
    folder_path = directory / folder
    folder_path.mkdir(parents=True, exist_ok=True)

print("All folders created successfully!")

# Q12. File Backup Manager

# Concept: shutil.copy2(), shutil.copytree()

# Requirements:

    # Accept a source folder.
    # Create a backup folder.
    # Copy all files and subfolders.
    # Preserve file metadata where supported.
    # Display backup completion status.

# Steps to Solve:

    # Accept or define a source directory.
    # Verify that the source directory exists.
    # Select a backup destination.
    # Use shutil.copytree() with an appropriate copy function.
    # Handle an existing destination directory.
    # Verify the copied files.
    # Display a backup summar

#_----------------------------------------------------------------------------------------------------------------------------------

import os
import shutil

# Source and backup folders
source_folder = "info_copy"
backup_folder = "backup_data"

# Check if source exists
if not os.path.exists(source_folder):
    raise FileNotFoundError(f"Source folder '{source_folder}' does not exist.")

# Handle existing backup directory
if os.path.exists(backup_folder):
    print("Backup folder already exists. Removing old backup...")
    shutil.rmtree(backup_folder)

# Copy folder with metadata preservation
shutil.copytree(
    source_folder,
    backup_folder,
    copy_function=shutil.copy2
)

# Verify backup
if os.path.exists(backup_folder):
    print("Backup completed successfully!")
else:
    print("Backup failed!")

# Backup summary
source_files = sum(len(files) for _, _, files in os.walk(source_folder))
backup_files = sum(len(files) for _, _, files in os.walk(backup_folder))

print("\n------ Backup Summary ------")
print(f"Source Folder : {source_folder}")
print(f"Backup Folder : {backup_folder}")
print(f"Files Copied  : {backup_files}")
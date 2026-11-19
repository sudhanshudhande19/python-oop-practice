# Q4. Copy an Entire Folder

# Concept: shutil.copytree()

# Requirements:

    # Create a folder.
    # Add at least two files.
    # Create a subfolder containing another file.
    # Copy the complete folder.
    # Verify the copied structure.

# Steps to Solve:

    # Create a practice directory.
    # Add sample files and a subdirectory.
    # Select a new destination directory.
    # Use shutil.copytree().
    # Check whether all files and subdirectories exist.
    # Display the result.

#--------------------------------------------------------------------------------------------------------------

import shutil

shutil.copytree('MyFiles','info_copy')
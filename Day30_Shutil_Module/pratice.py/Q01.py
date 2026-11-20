# Q1. Copy a Text File

# Concept: shutil.copy()

# Requirements:

    # Create a text file.
    # Copy it to another location.
    # Verify that the copied file exists.
    # Display a success message.

# Steps to Solve:

    # Import shutil.
    # Create a source text file with some content.
    # Select a destination path.
    # Use shutil.copy().
    # Verify the destination file.
    # Display the result.

#-----------------------------------------------------------------------------------------------------------

import shutil

shutil.copy('text.txt','text2.txt')
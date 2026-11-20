# Q3. Copy Only File Contents

# Concept: shutil.copyfile()

# Requirements:

    # Create a source file.
    # Copy its contents into a new file.
    # Read both files.
    # Verify that their contents match.

# Steps to Solve:

    # Create a source file.
    # Write some text into it.
    # Use shutil.copyfile().
    # Open both files in read mode.
    # Compare their contents.
    # Display whether the copying was successful.

#----------------------------------------------------------------------------------------------

import shutil

shutil.copyfile('sample.txt','source.md')
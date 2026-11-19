# Concept: shutil.move()

# Requirements:

    # Create a source file.
    # Create a destination folder.
    # Move the source file into the destination folder.
    # Verify the new location.

# Steps to Solve:

    # Create a file.
    # Create a destination directory.
    # Use shutil.move().
    # Check the original path.
    # Check the destination path.
    # Display the result.

#_----------------------------------------------------------------------------------------------

import shutil

shutil.move('sample.txt','info_copy/sample.txt')
shutil.move('text.txt','info_copy/text.txt')
shutil.move('text2.txt','info_copy/text2.txt')
shutil.move('source.md','info_copy/source.md')

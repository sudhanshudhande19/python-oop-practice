# Q6. Rename a File Using Shutil

# Concept: shutil.move()

# Requirements:

    # Create a file with an old name.
    # Rename it using shutil.move().
    # Check whether the old file exists.
    # Check whether the renamed file exists.

# Steps to Solve:

    # Create a sample file.
    # Decide its new name.
    # Use shutil.move() with the new path.
    # Verify the old path.
    # Verify the new path.
    # Display the renamed file information.

#-----------------------------------------------------------------------------------------------------------


import shutil

shutil.move('info_copy/text.txt','text.txt')
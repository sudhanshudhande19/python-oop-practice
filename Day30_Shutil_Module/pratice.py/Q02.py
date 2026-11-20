# Q2. Copy a File with Metadata

# Concept: shutil.copy2()

# Requirements:

    # Create a sample file.
    # Copy it using copy2().
    # Compare the source and destination modification times.
    # Display both file paths.

# Steps to Solve:

    # Import shutil and os.
    # Create a sample source file.
    # Copy it using shutil.copy2().
    # Read the modification time of both files.
    # Compare the values.
    # Display the result.

#-------------------------------------------------------------------------------------------------------------------


import shutil

shutil.copy2('text.txt','sample.txt')
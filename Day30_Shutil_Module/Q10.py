# Q10. Extract a ZIP File

# Concept: shutil.unpack_archive()

# Requirements:

    # Use an existing ZIP archive.
    # Extract it into a new folder.
    # Verify the extracted files.
    # Display the extraction result.

# Steps to Solve:

    # Create or select a practice ZIP archive.
    # Choose a new extraction directory.
    # Use shutil.unpack_archive().
    # Check the extracted directory.
    # Verify the expected files.
    # Display the result.

#----------------------------------------------------------------------------------------------------


import shutil

shutil.unpack_archive(
    'backup.zip',
    'extracted_data'
                      
)
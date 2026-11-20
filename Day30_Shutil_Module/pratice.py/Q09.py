# Q9. Create a ZIP Backup

# Concept: shutil.make_archive()

# Requirements:

    # Create a folder containing sample files.
    # Create a ZIP archive from that folder.
    # Verify that the ZIP file exists.
    # Display a success message.

# Steps to Solve:

    # Create a practice folder.
    # Add multiple sample files.
    # Select an archive name.
    # Use shutil.make_archive().
    # Check whether the archive exists.
    # Display its path.

#------------------------------------------------------------------------------------------------------

import shutil

kk = shutil.make_archive(
    'backup',
    'zip',
)
print(kk)
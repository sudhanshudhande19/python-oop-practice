# Q8. Display Disk Information

# Concept: shutil.disk_usage()

# Requirements:

    # Check disk usage for a drive.
    # Display total space.
    # Display used space.
    # Display free space.
    # Convert bytes into GB for easier reading.

# Steps to Solve:

    # Import shutil
    # Pass a valid drive path to disk_usage().
    # Store the returned information.
    # Read total, used, and free values.
    # Convert bytes into GB.
    # Display all three values.


#---------------------------------------------------------------------------------------------------

import shutil

location =shutil.disk_usage('info_copy/source.md')

print(f'Total Sapce = {location.total}')
print(f'Used Space = {location.used}')
print(f'Free Space = {location.free}')
# Q7. Find Python Executable

# Concept: shutil.which()

# Requirements:

    # Search for the Python executable.
    # Display its location.
    # Handle the case when it is not found.

# Steps to Solve:

    # Import shutil.
    # Call shutil.which() with the executable name.
    # Store the returned value.
    # Check whether the value is None.
    # Display the location or a not-found message.

#----------------------------------------------------------------------------------------------------


import shutil

location = shutil.which('python')
print(location)
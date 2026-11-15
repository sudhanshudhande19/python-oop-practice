# Concept: time.localtime()

# Requirements:

    # Get the current local time.
    # Display year, month, and day.
    # Display hour, minute, and second.
    # Call time.localtime().
    # Store the returned object.
    # Access the required attributes.
    # Print each value separately.

#---------------------------------------------------------------------------------

import time

current = time.localtime()

print(current)
print(f'{current.tm_year}-{current.tm_mon}-{current.tm_mday}')
print(f'{current.tm_hour}:{current.tm_min}:{current.tm_sec}')
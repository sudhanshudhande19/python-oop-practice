# Q5. Display Current Time

# Concept: time.localtime() and time.strftime()

# Requirements:

    # Display the current local time.
    # Format the time in hours, minutes, and seconds.

# Steps to Solve:

    # Import the time module.
    # Get the current local time.
    # Format it using time.strftime().
    # Display the formatted time.

#----------------------------------------------------------------------------------------------


import time

loc_time = time.localtime()

loc_time = time.strftime('%H:%M:%S')

print(loc_time)
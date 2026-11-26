# Concept: time.strftime()

# Requirements:

    # Get the current local time.
    # Display time in 12-hour format.
    # Show AM or PM.
    # Display the complete date.
    # Get the current local time.
    # Use %I for the 12-hour clock.
    # Use %M and %S for minutes and seconds.
    # Use %p for AM/PM.
    # Format and display the result.

#_-----------------------------------------------------------------------------------------


import time

current_time = time.localtime()
current_time = time.strftime('%I:%M:%S %p')

print(current_time)
# Concept: time.strftime()

# Requirements:

    # Display date in DD-MM-YYYY format.
    # Display time in HH:MM:SS format.
    # Display the weekday name.
    # Get the current local time.
    # Use time.strftime().
    # Select the appropriate formatting codes.
    # Display the formatted values.

#------------------------------------------------------------------------------

import time

current_date = time.strftime('%d-%m-%Y')
current_time = time.strftime('%H:%M:%S')
print(current_date)
print(current_time)
# Concept: time.ctime()

# Requirements:

    # Get the current timestamp.
    # Convert it into readable date and time.
    # Display the result.
    # Get the timestamp.
    # Pass it to time.ctime().
    # Store the result.
    # Print the readable date and time.

#-----------------------------------------------------------------------


import time
current_time = time.time()
print(time.ctime(current_time))
# Concept: time.localtime(), time.strftime(), time.sleep()

# Requirements:

    # Display the current time.
    # Update the time every second.
    # Continue displaying the clock.
    # Create an infinite loop.
    # Get the current local time.
    # Format it as HH:MM:SS.
    # Display the updated time.
    # Pause execution for one second.
    # Refresh the display.

#--------------------------------------------------------------------------------------------------


import time

current_time = time.localtime()

current_time = time.strftime('%H:%M:%S')
time.sleep(1)
print(current_time)
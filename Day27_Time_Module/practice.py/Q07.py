# Concept: time.sleep()

# Requirements:

    # Ask the user to enter countdown seconds.
    # Display the remaining seconds.
    # Decrease the value every second.
    # Display a completion message at zero.
    # Take the countdown duration from the user.
    # Start a loop from the entered number.
    # Display the remaining time.
    # Pause for one second.
    # Decrease the counter.
    # Display a completion message.

#__-------------------------------------------------------------------------------------------

import time

seconds = int(input('Enter countown seconds ='))

while seconds > 0:
    print(f'Remaing = {seconds},seconds')
    time.sleep(1)
    seconds -= 1

print('Countdown completed')
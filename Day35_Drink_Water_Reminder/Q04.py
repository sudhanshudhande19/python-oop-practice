# Q4. Repeat a Reminder Three Times

# Concept: Loops

# Requirements:

    # Display a water reminder three times.
    # Wait five seconds between reminders.

# Steps to Solve:

    # Create a counter.
    # Use a loop that runs three times.
    # Display the reminder inside the loop.
    # Add a five-second delay between reminders.
    # Stop after the third reminder.

#---------------------------------------------------------------------------------------------------------

import time

count = 1
while count <= 3:
    print(f'water reminder three times')
    time.sleep(5)
    count += 1


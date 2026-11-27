# Q8. Reminder Counter

# Concept: Variables and loops

# Requirements:

    # Count how many reminders have been displayed.
    # Display the reminder number each time.
    # Stop after five reminders.

# Steps to Solve:

    # Create a counter variable.
    # Start the counter at zero.
    # Use a loop that runs five times.
    # Increase the counter after each reminder.
    # Display the counter with the reminder.

#--------------------------------------------------------------------------------------------------------------------

import time

count = 0

while count < 5:
        count += 1
        print(f"Reminder {count}: Drink Water!")
        time.sleep(2)

print("All 5 reminders completed.")

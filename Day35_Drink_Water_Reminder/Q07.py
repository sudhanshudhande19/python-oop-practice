# Q7. Continuous Water Reminder

# Concept: while loop

# Requirements:

    # Create a reminder that repeats continuously.
    # Wait for a fixed interval.
    # Allow the user to stop the application.

# Steps to Solve:

    # Create a while loop.
    # Wait for the selected interval.
    # Display the reminder.
    # Repeat the process.
    # Stop the program using an appropriate exit mechanism.

#------------------------------------------------------------------------------------------------------------------


import time

try:
    while True:
        time.sleep(10)
        print("Reminder: Drink Water!")

except KeyboardInterrupt:
    print("\nReminder stopped by user.")
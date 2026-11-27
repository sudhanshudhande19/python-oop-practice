# Q11. Customizable Water Reminder

# Concept: Functions, loops, and time

# Requirements:

    # Allow the user to select the reminder interval.
    # Allow the user to select the number of reminders.
    # Display reminders automatically.
    # Display the reminder count.

# Steps to Solve:

    # Create a function to accept reminder settings.
    # Validate the interval.
    # Validate the reminder count.
    # Create a loop for the selected number of reminders.
    # Wait for the selected interval.
    # Display each reminder with its number.
    # Display a completion message.


#------------------------------------------------------------------------------------------------------------------

import time

def water_reminder(interval, count):

    if interval <= 0:
        print("Invalid Interval! Enter a positive number.")
        return

    if count <= 0:
        print("Invalid Reminder Count! Enter a positive number.")
        return

    for i in range(1, count + 1):
        time.sleep(interval)
        print(f' Reminder {i}: Drink Water!')

    print("All reminders completed.")

interval = int(input("Enter Reminder Interval (seconds): "))
count = int(input("Enter Number of Reminders: "))

water_reminder(interval, count)
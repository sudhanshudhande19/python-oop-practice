# Q6. User-Defined Reminder Interval

# Concept: User input and time delay

# Requirements:

    # Ask the user to enter a reminder interval in seconds.
    # Wait for the entered interval.
    # Display the reminder.

# Steps to Solve:

    # Ask the user to enter the interval.
    # Convert the input into an integer.
    # Validate that the interval is positive.
    # Wait for the selected duration.
    # Display the reminder.

#-----------------------------------------------------------------------------------------------------------------------------


import time


interval = int(input("Enter reminder interval in seconds: "))


if interval > 0:
    print(f"Reminder will be shown after {interval} seconds...")
    
    time.sleep(interval)
    
    print(" Reminder: Time is up!")
else:
    print("Please enter a positive number.")
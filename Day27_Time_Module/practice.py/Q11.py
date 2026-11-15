# Concept: time.sleep()

# Requirements:

    # Ask the user for a reminder message.
    # Ask how many seconds to wait.
    # Wait for the specified duration.
    # Display the reminder message.
    # Take a message from the user.
    # Take the delay in seconds.
    # Use time.sleep() with the entered duration.
    # Display the reminder.

#-----------------------------------------------------------------------------------


import time

# Take reminder message from user
message = input("Enter Reminder Message: ")

# Take waiting time in seconds
seconds = int(input("Enter Time in Seconds: "))

print("Wait...")

# Pause program
time.sleep(seconds)

# Display reminder
print("Reminder:", message)
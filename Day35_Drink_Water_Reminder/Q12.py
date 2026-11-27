# Q12. Water Reminder with Current Time

# Concept: Time formatting and application logic

# Requirements:

    # Display the current time with each reminder.
    # Repeat reminders at a fixed interval.
    # Count the total reminders.
    # Stop after the selected number of reminders.

# Steps to Solve:

    # Create a function to get the current time.
    # Format the time using time.strftime().
    # Create a reminder counter.
    # Wait for the selected interval.
    # Display the reminder and current time.
    # Repeat until the selected count is reached.
    # Display the total number of reminders.

#--------------------------------------------------------------------------------------------------------------
import time

def get_current_time():
    return time.strftime("%H:%M:%S")


interval = int(input("Enter reminder interval (seconds): "))
count = int(input("Enter number of reminders: "))


if interval <= 0 or count <= 0:
    print("Invalid input! Interval and count must be greater than 0.")
else:
    for i in range(1, count + 1):
        time.sleep(interval)

        current_time = get_current_time()

        print(f"Reminder {i}: Drink Water!")
        print(f"Current Time: {current_time}")
        print("-" * 30)

    print(f"Total Reminders Displayed: {count}")
    print("All reminders completed.")
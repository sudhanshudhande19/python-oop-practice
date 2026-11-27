import time

# Global Variables
reminder_interval = 5
total_reminders = 0


# Function to get current time
def get_current_time():
    return time.strftime("%H:%M:%S")


# Function to set reminder interval
def set_interval():
    global reminder_interval

    try:
        interval = int(input("Enter Reminder Interval (seconds): "))

        if interval > 0:
            reminder_interval = interval
            print(f"Reminder interval set to {interval} seconds.")

        else:
            print("Interval must be greater than 0.")

    except ValueError:
        print("Please enter a valid number.")


# Function to start reminders
def start_reminder():
    global total_reminders

    try:
        count = int(input("Enter Number of Reminders: "))

        if count <= 0:
            print("Reminder count must be greater than 0.")
            return

        print("\n Water Reminder Started...")
        print("Press Ctrl + C to stop safely.\n")

        for i in range(1, count + 1):
            time.sleep(reminder_interval)

            current_time = get_current_time()

            print(
                f"Reminder {i}: Drink Water! | Time: {current_time}"
            )

            total_reminders += 1

        print("\nAll reminders completed.")
        print(f"Total Reminders Shown: {total_reminders}")

    except ValueError:
        print(" Invalid reminder count.")

    except KeyboardInterrupt:
        print("\nReminder stopped safely by user.")
        print(f"Total Reminders Shown: {total_reminders}")


# Function to view reminder count
def view_count():
    print(f"\nTotal Reminders Displayed: {total_reminders}")


# Main Menu
def main():

    print("=" * 40)
    print("      DRINK WATER REMINDER")
    print("=" * 40)

    while True:

        print("\n1. Start Reminder")
        print("2. Set Reminder Interval")
        print("3. View Reminder Count")
        print("4. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                start_reminder()

            elif choice == 2:
                set_interval()

            elif choice == 3:
                view_count()

            elif choice == 4:
                print("\nThank you for using Drink Water Reminder.")
                break

            else:
                print("Please select a valid option (1-4).")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Program Starts Here
main()

import time

print("=" * 66)
print("                    SMART TIME UTILITY")
print("=" * 66)

print()
print("\n1. Current Date and Time")
print("2. Digital Clock")
print("3. Countdown Timer")
print("4. Stopwatch")
print("5. Current Timestamp")
print("6. Execution Time Calculator")
print("7. Exit")

while True:


    option = int(input("\nEnter Your Choice: "))

    # Current Date and Time
    if option == 1:
        current_date = time.strftime("%d-%m-%Y")
        current_time = time.strftime("%H:%M:%S")

        print("\nDate =", current_date)
        print("Time =", current_time)
        print("-" * 40)

    # Digital Clock
    elif option == 2:
        print("\nLoading Digital Clock...")
        time.sleep(1)

        digital_time = time.strftime("%I:%M:%S %p")
        print("Digital Clock =", digital_time)
        print("-" * 40)

    # Countdown Timer
    elif option == 3:
        count_time = int(input("Enter Countdown Seconds: "))

        print("\nCountdown Started...")
        while count_time > 0:
            print("Remaining:", count_time, "seconds")
            time.sleep(1)
            count_time -= 1

        print("Countdown Completed!")
        print("-" * 40)

    # Stopwatch
    elif option == 4:
        input("\nPress Enter To Start Stopwatch...")
        start_time = time.perf_counter()

        input("Press Enter To Stop Stopwatch...")
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print("Elapsed Time =", round(elapsed_time, 4), "seconds")
        print("-" * 40)

    # Current Timestamp
    elif option == 5:
        timestamp = time.time()

        print("\nCurrent Timestamp =", timestamp)
        print("-" * 40)

    # Execution Time Calculator
    elif option == 6:
        print("\nMeasuring Loop Execution Time...")

        start_time = time.perf_counter()

        for i in range(100000):
            pass

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print("Execution Time =", execution_time, "seconds")
        print("-" * 40)

    # Exit
    elif option == 7:
        print("\nThank You For Using Smart Time Utility!")
        break

    # Invalid Choice
    else:
        print("\nInvalid Choice! Please Try Again.")
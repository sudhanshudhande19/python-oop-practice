# Q11. Cached Data Calculator

# Concept: Caching and application logic

# Requirements:

    # Create a calculator with cached operations.
    # Support addition, multiplication, and power calculations.
    # Reuse results for repeated inputs.
    # Display cache information.

# Steps to Solve:

    # Create separate functions for each operation.
    # Apply lru_cache to suitable functions.
    # Accept numbers from the user.
    # Allow the user to select an operation.
    # Display the calculation result.
    # Repeat calculations using the same arguments.
    # Display cache statistics.
    # Add input validation.


#------------------------------------------------------------------------------------------------------------------------------------------

from functools import lru_cache

# Cached Functions
@lru_cache(maxsize=50)
def add(a, b):
    return a + b

@lru_cache(maxsize=50)
def multiply(a, b):
    return a * b

@lru_cache(maxsize=50)
def power(a, b):
    return a ** b

while True:
    print("\n===== Cached Calculator =====")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Power")
    print("4. Show Cache Info")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Calculator Closed!")
        break

    elif choice == "4":
        print("\nAddition Cache :", add.cache_info())
        print("Multiplication Cache :", multiply.cache_info())
        print("Power Cache :", power.cache_info())
        continue

    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == "1":
        print("Result =", add(a, b))

    elif choice == "2":
        print("Result =", multiply(a, b))

    elif choice == "3":
        print("Result =", power(a, b))

    else:
        print("Invalid Choice!")

# Concept: sys.argv, type conversion

# Requirements:

    # Accept two numbers from the terminal.
    # Accept an operation such as add, subtract, multiply, or divide.
    # Perform the selected operation.
    # Display the result.
    # Handle division by zero.

    # Accept the first number.
    # Accept the second number.
    # Accept the operation.
    # Convert the numbers into appropriate numeric types.
    # Use conditional statements to select the operation.
    # Perform the calculation.
    # Handle invalid operations and division by zero.

#--------------------------------------------------------------------------------------------


import sys

# Check if correct number of arguments are provided
if len(sys.argv) != 4:
    print("Usage: python calculator.py <num1> <num2> <operation>")
    print("Example: python calculator.py 10 5 add")
    sys.exit()

try:
    # Accept numbers from command line
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    # Accept operation
    operation = sys.argv[3].lower()

    # Perform calculation
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            sys.exit()
        result = num1 / num2
    else:
        print("Error: Invalid operation.")
        print("Valid operations: add, subtract, multiply, divide")
        sys.exit()

    print(f"Result = {result}")

except ValueError:
    print("Error: Please enter valid numeric values.")
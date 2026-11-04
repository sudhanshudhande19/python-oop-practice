# Create a decorator that prints "Calculating..." before a calculator function executes.

# Create functions for:

# Addition
# Subtraction
# Multiplication
# Division

# Handle division by zero appropriately.
#-------------------------------------------------------------------------------------------------------
def calculator_decorator(func):
    def wrapper(a, b):
        print("Calculating...")
        return func(a, b)
    return wrapper


@calculator_decorator
def add(a, b):
    return a + b


@calculator_decorator
def subtract(a, b):
    return a - b


@calculator_decorator
def multiply(a, b):
    return a * b


@calculator_decorator
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


# Test cases
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Division:", divide(10, 0))
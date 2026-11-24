# Q3. Cache Addition Results

# Concept: Multiple function arguments

# Requirements:

    # Create a function that adds two numbers.
    # Apply caching.
    # Call it with repeated and different arguments.

# Steps to Solve:

    # Import the cache decorator.
    # Create an add function.
    # Accept two arguments.
    # Return their sum.
     # Apply the decorator.
    # Call the function with (5, 10) twice.
    # Call it with different arguments.
    # Observe which results are reused.

#-----------------------------------------------------------------------------------------------------


from functools import cache

@cache

def add(a,b):
    return a + b

print(add(6,6))
print(add(4,9))
print(add(6,6))
# Q1. Create Your First Generator

# Concept: Generator function and yield

# Requirements:

    # Create a generator function.
    # Generate five numbers.
    # Display each generated value.

# Steps to Solve:

    # Create a function named numbers.
    # Use yield to produce five integer values.
    # Call the generator function.
    # Store the returned generator object.
    # Use a for loop to display the values.


#---------------------------------------------------------------------------------------------


def numbers():
    yield 1
    yield 2 
    yield 3 
    yield 4
    yield 5

for i in numbers():
    print(i)
# Concept: sys.argv, type conversion

# Requirements:

    # Accept two numbers from the terminal.
    # Convert them into integers.
    # Calculate their sum.
    # Display the result.
    # Import sys.
    # Check whether two numbers were provided.
    # Access both arguments.
    # Convert them into integers.
    # Calculate the sum.
    # Display the result.

#------------------------------------------------------------------------


import sys


num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print('sum =',num1 +num2)
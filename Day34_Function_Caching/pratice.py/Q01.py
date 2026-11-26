# Q1. Understand Repeated Function Calls

# Concept: Function execution

# Requirements:

    # Create a function that calculates a square.
    # Call it three times with the same number.
    # Display the results.

# Steps to Solve:

    # Create a function named square.
    # Accept one integer argument.
    # Calculate its square.
    # Display the result.
    # Call the function three times using the same argument.
    # Observe how many times the function executes.


#----------------------------------------------------------------------------------------------------------------------------------



def square(n):
    if n > 0:
        return n * n
    else:
        print('Enter The Interger Number')


print(square(5))
print(square(5))
print(square(5))
# Q9. Calculate Total Until Negative Input

# Concept: Walrus Operator with while

# Requirements:

    # Continuously accept numbers from the user.
    # Add positive numbers to a total.
    # Stop when a negative number is entered.
    # Display the total.

# Steps to Solve:

    # Initialize a total variable.
    # Use a while loop.
    # Accept input inside the loop condition.
    # Assign the input using :=.
    # Add valid positive numbers to the total.
    # Stop when a negative number is entered.
    # Display the total.

#_-------------------------------------------------------------------------------------------------------------------


while (total_var := int(input('Enter The number ='))) != 0:
    print(f'Positive Number')

print('Negative Number')
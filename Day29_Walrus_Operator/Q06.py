# Q6. Input Until Zero

# Concept: Walrus Operator with while

# Requirements:

    # Continuously ask the user for a number.
    # Display the entered number.
    # Stop when the user enters zero.

# Steps to Solve:

    # Create a while loop.
    # Take input inside the loop condition.
    # Assign the input using :=.
    # Continue while the number is not zero.
    # Display a completion message after the loop.

#-------------------------------------------------------------------------------------------------------



while (num := int(input('Enter The Number ='))) !=0:
    print('you entered =',num)

print('Program ended')
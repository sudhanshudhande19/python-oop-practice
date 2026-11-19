# Q5. Check Positive Number

# Concept: Assignment expression

# Requirements:

    # Assign a number using :=.
    # Check whether it is positive, negative, or zero.
    # Display the result.

# Steps to Solve:

    # Assign a number using the Walrus Operator.
    # Use conditional statements.
    # Check whether the number is greater than zero.
    # Check whether it is less than zero.
    # Handle zero separately.

#-----------------------------------------------------------------------------------------------------------------------

num1 = int(input('Enter The Number = '))

if (num := num1) > 0:
    print(f'{num1} is Greater Than Zero')

else:
     print(f'{num1} is Less Than Zero')
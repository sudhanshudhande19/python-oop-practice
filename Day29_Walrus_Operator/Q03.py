# Q3. Calculate String Length

# Concept: len() with :=

# Requirements:

    # Take a string.
    # Calculate its length using the Walrus Operator.
    # Display the length.
    # Check whether the string contains more than 5 characters.

# Steps to Solve:

    # Create a string variable.
    # Calculate its length using len().
    # Assign the result using :=.
    # Check the length.
    # Display the appropriate message

#---------------------------------------------------------------------------------------------------

num = 'sudhanshu'

if (length := len(num)) > 2:
    print('List =',num)

    print('Length :',length)


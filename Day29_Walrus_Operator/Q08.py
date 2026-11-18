# Q8. Filter Large Numbers

# Concept: Assignment expression with list comprehension

# Requirements:

    # Create a list of numbers.
    # Calculate the square of each number.
    # Store each square using :=.
    # Select squares greater than 25.

# Steps to Solve:

    # Create a list of integers.
    # Use a list comprehension.
    # Calculate each square.
    # Store the square using :=.
    # Filter values greater than 25.
    # Display the final list.

#--------------------------------------------------------------------------------------------------------

num = [1,2,3,4,5,6,7,8,9]

result =  [square for number in  num if (square := number * number) > 25]
print(result)
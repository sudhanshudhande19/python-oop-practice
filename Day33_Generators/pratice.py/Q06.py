# Q6. Generate Multiplication Table

# Concept: Generators and loops

# Requirements:

    # Generate a multiplication table for a user-entered number.
    # Produce ten results.
    # Display the complete table.

# Steps to Solve:

    # Ask the user to enter a number.
    # Create a generator function that accepts the number.
    # Use a loop from 1 to 10.
    # Calculate the multiplication result.
    # Use yield to produce each result.
    # Display the table using a for loop.

#---------------------------------------------------------------------------------------------------------------------------

user  = int(input('Enter the Number = '))

def generator():
    for num in range(1,10+1):
        total = user * num
        yield total

for mul in generator():
    print(mul)

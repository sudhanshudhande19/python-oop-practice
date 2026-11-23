# Q4. Generate Squares

# Concept: Mathematical operations with generators

# Requirements:

    # Generate squares of numbers from 1 to 10.
    # Produce each square separately.
    # Display the results.

# Steps to Solve:

    # Create a generator function.
    # Use a loop from 1 to 10.
    # Calculate the square of each number.
    # Use yield to produce the square.
    # Iterate over the generator.

#----------------------------------------------------------------------------------------------------------------

def generator():
    for num in range(1,10+1):
        sum = num * num
        
        yield sum

for squares in generator():
    print(squares)
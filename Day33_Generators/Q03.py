# Q3. Generate Even Numbers

# Concept: Conditions with yield

# Requirements:

    # Generate even numbers between 1 and 20.
    # Produce values one at a time.
    # Display all generated values.

# Steps to Solve:

    # Create a generator function.
    # Use a loop from 1 to 20.
    # Check whether each number is divisible by 2.
    # Use yield for even numbers.
    # Display the values using a for loop.

#--------------------------------------------------------------------------------------------


def generator():
    for i  in range(1,20):
        if i %2 == 0:
            yield i

for num in generator():
    print(num)



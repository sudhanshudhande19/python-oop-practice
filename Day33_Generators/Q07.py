# Q7. Generate Fibonacci Numbers

# Concept: Generator state

# Requirements:

    # Generate Fibonacci numbers.
    # Allow the user to specify how many numbers are required.
    # Display the sequence.

# Steps to Solve:

    # Ask the user for the number of terms.
    # Create a generator function.
    # Initialize the first two Fibonacci values.
    # Use a loop for the requested number of terms.
    # Use yield to produce each value.
    # Update the two variables after each yield.
    # Display the sequence.

#-------------------------------------------------------------------------------------------------------------------------


user = int(input('Enter The Number = '))

def generator(user):
    a ,b = 0,1

    for num in range(user):
        yield a
        a , b = b , a + b 

for total in generator(user):
    print(total)

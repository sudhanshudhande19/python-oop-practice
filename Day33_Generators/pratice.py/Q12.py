# Q12. Data Batch Generator

# Concept: Generators and data processing

# Requirements:

    # Create a list of 100 numbers.
    # Generate data in batches of 10.
    # Display each batch.
    # Handle the final batch correctly.

# Steps to Solve:

    # Create a list containing 100 numbers.
    # Create a generator function that accepts the list and batch size.
    # Use a loop to identify batch boundaries.
    # Use yield to produce each batch.
    # Iterate through the generator.
    # Display each batch.
    # Test the function with a list whose length is not divisible by the batch size.



#---------------------------------------------------------------------------------------------------------------------------------------------

# Create list of 100 numbers
numbers = list(range(1, 101))


def batch_generator(data, batch_size):

    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]



for batch in batch_generator(numbers, 10):
    print(batch)
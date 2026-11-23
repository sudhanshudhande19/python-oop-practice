# Q5. Use next() Function

# Concept: Generator iteration

# Requirements:

    # Create a generator with three values.
    # Retrieve values using next().
    # Display each value separately.

# Steps to Solve:

    # Create a generator function.
    # Use yield to produce three values.
    # Create a generator object.
    # Call next() three times.
    # Observe the order of returned values.


#-----------------------------------------------------------------------------------------------------------------


def genarator():
    yield 55
    yield 96
    yield 32


num = genarator()

print(next(num))
print(next(num))
print(next(num))
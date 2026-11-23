# Q10. Handle Generator Exhaustion

# Concept: StopIteration

# Requirements:

    # Create a generator with three values.
    # Retrieve all values using next().
    # Handle the exhausted generator safely.

# Steps to Solve:

    # Create a generator function with three yield statements.
    # Create its generator object.
    # Use next() to retrieve values.
    # Attempt to retrieve one additional value.
    # Handle StopIteration using try-except.
    # Display a suitable completion message.


#--------------------------------------------------------------------------------------------------------------


def generator():

    yield 10
    yield 20
    yield 30

num = generator()
try :

    print(next(num))
    print(next(num))
    print(next(num))
    print(next(num))

except StopIteration:
    print('Generator exhausted. No more values available ') 
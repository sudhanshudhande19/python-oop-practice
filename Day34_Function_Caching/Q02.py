# Q2. Use Your First Cache Decorator

# Concept: functools.cache

# Requirements:

    # Import cache.
    # Create a square function.
    # Apply the cache decorator.
    # Call the function repeatedly.

# Steps to Solve:

    # Import cache from functools.
    # Create a function named square.
    # Add the @cache decorator.
    # Print a message inside the function to track execution.
    # Call the function three times with the same argument.
    # Observe when the calculation message appears.



#-------------------------------------------------------------------------------------------------------------------------------



from functools import cache

@cache
def square(n):
    print("Calculating square...")
    return n * n

print(square(5))
print(square(5))
print(square(5))
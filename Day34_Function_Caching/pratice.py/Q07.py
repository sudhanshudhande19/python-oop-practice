# Q7. Fibonacci with Caching

# Concept: Recursion and memoization

# Requirements:

    # Create a recursive Fibonacci function.
    # Apply lru_cache.
    # Generate Fibonacci values.
    # Inspect cache statistics.

# Steps to Solve:

    # Import lru_cache.
    # Create a function named fibonacci.
    # Add base cases for 0 and 1.
    # Calculate the previous two Fibonacci values recursively.
    # Apply @lru_cache.
    # Call the function with different values.
    # Display the result and cache information.


#------------------------------------------------------------------------------------------------------------



from functools import lru_cache

@lru_cache(maxsize=100)

def fibonacci(n):

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(10) =", fibonacci(10))
print("Fibonacci(20) =", fibonacci(20))
print("Fibonacci(30) =", fibonacci(30))


print("\nCache Information:")
print(fibonacci.cache_info())

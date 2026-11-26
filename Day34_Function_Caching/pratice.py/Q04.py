# Q4. Use lru_cache

# Concept: LRU caching

# Requirements:

    # Import lru_cache.
    # Create a multiplication function.
    # Set a cache size.
    # Test repeated calls.

# Steps to Solve:

    # Import lru_cache.
    # Create a function named multiply.
    # Apply @lru_cache(maxsize=5).
    # Accept two integer arguments.
    # Return their product.
    # Call the function using repeated arguments.
    # Observe the results.

#--------------------------------------------------------------------------------------------------------------


from functools import lru_cache

@lru_cache(maxsize=5)
def multiply(a, b):
    print("Calculating...")
    return a * b

print(multiply(5, 6))
print(multiply(5, 6))
print(multiply(5, 6))
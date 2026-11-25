# Q6. Clear the Cache

# Concept: cache_clear()

# Requirements:

    # Create a cached square function.
    # Store multiple results.
    # Clear the cache.
    # Check cache information again.

# Steps to Solve:

    # Create a function with @lru_cache.
    # Call it using different arguments.
    # Display cache_info().
    # Call cache_clear().
    # Display cache_info() again.
    # Compare the cache information before and after clearing.


#-----------------------------------------------------------------------------------------------------------------------------

from functools import lru_cache

@lru_cache(maxsize=10)
def square(n):
    return n * n


square(5)
square(10)
square(15)
square(20)


print("Before clearing:")
print(square.cache_info())


square.cache_clear()

print("\nAfter clearing:")
print(square.cache_info())
# Q5. Understand Cache Information

# Concept: cache_info()

# Requirements:

    # Create a cached function.
    # Call it multiple times.
    # Display cache statistics.

# Steps to Solve:

    # Create a function with @lru_cache.
    # Call it with the same argument more than once.
    # Call it with a different argument.
    # Use cache_info().
    # Identify hits, misses, maxsize, and currsize.

#-------------------------------------------------------------------------------------------------------


from functools import lru_cache

@lru_cache(maxsize = 5)
def cached(n):
    return n * n

cached(5)
cached(5)
cached(10)

print(cached.cache_info())
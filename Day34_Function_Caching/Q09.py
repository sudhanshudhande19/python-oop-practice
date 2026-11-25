# Q9. Compare Cached and Non-Cached Functions

# Concept: Performance comparison

# Requirements:

    # Create one normal function.
    # Create one cached function.
    # Call both repeatedly.
    # Compare their execution time.

# Steps to Solve:

    # Create a function that performs a moderately expensive calculation.
    # Create a normal version.
    # Create a cached version.
    # Use time.perf_counter() to measure execution time.
    # Call each function with repeated inputs.
    # Compare the results and execution times.
    # Explain why caching may help repeated calls.

#------------------------------------------------------------------------------------------------------------------

from functools import lru_cache 
import time

def normal(n):
    return n + n


@lru_cache(maxsize=100)
def cache(n):

    return n + n

n = 35

# Measure normal function
start = time.perf_counter()
result = normal(n)
end = time.perf_counter()

normal_time = start - end

# Measure cached function
start = time.perf_counter()
result2 = cache(n)
end = time.perf_counter()

cache_time = start - end

print("Normal Function Result :", result)
print("Cached Function Result :", result2)

print("\nNormal Function Time :", normal_time)
print("Cached Function Time :", cache_time)

print("\nCache Information:")
print(cache.cache_info())
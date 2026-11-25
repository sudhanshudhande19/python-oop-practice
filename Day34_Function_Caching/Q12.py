# Q12. Smart Fibonacci Analyzer

# Concept: Recursion, caching, and performance

# Requirements:

    # Generate Fibonacci numbers using recursion.
    # Create a cached version.
    # Compare the two approaches.
    # Display cache statistics.

# Steps to Solve:

    # Create a normal recursive Fibonacci function.
    # Create a second Fibonacci function with lru_cache.
    # Ask the user for a Fibonacci position.
    # Measure the execution time of both versions.
    # Display both results.
    # Display the cached function's statistics.
    # Explain the difference in repeated calculat
    # Test with several input values.

#----------------------------------------------------------------------------------------------------------

from functools import lru_cache
import time


def fibonacci_normal(n):
    if n < 2:
        return n
    return fibonacci_normal(n - 1) + fibonacci_normal(n - 2)


@lru_cache(maxsize=100)
def fibonacci_cached(n):
    if n < 2:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


n = int(input("Enter Fibonacci Position: "))


start = time.perf_counter()
normal_result = fibonacci_normal(n)
normal_time = time.perf_counter() - start


start = time.perf_counter()
cached_result = fibonacci_cached(n)
cached_time = time.perf_counter() - start


print("\n===== Results =====")
print("Normal Fibonacci :", normal_result)
print("Cached Fibonacci :", cached_result)

print("\n===== Execution Time =====")
print(f"Normal Version : {normal_time:.6f} seconds")
print(f"Cached Version : {cached_time:.6f} seconds")

print("\n===== Cache Statistics =====")
print(fibonacci_cached.cache_info())
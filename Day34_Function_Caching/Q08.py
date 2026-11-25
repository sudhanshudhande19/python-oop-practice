# Q8. Understand Cache Size

# Concept: maxsize

# Requirements:

    # Create an LRU cached function.
    # Set maxsize=3.
    # Call the function with several different arguments.
    # Observe the current cache size.

# Steps to Solve:

    # Create a function with @lru_cache(maxsize=3).
    # Call it with at least five different arguments.
    # Display cache_info().
    # Check the currsize value.
    # Repeat some earlier calls.
    # Observe cache hits and misses.

#------------------------------------------------------------------------------------------------------------------------


from functools import lru_cache

@lru_cache(maxsize=3)

def LRU(n):
    return n + n

LRU(10)
LRU(20)
LRU(30)


LRU(40)  
LRU(50)  

print("After 5 different calls:")
print(LRU.cache_info())

# Repeat earlier calls
LRU(30)  
LRU(10)  

print("\nAfter repeated calls:")
print(LRU.cache_info())
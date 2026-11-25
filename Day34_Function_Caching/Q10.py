# Q10. Understand Hashable Arguments

# Concept: Cache keys and hashability

# Requirements:

    # Create a cached function with integer arguments.
    # Test it with a list argument.
    # Understand why some arguments cannot be cached directly.

# Steps to Solve:

    # Create a function using @cache.
    # Call it with integer arguments.
    # Try calling it with a list.
    # Observe the resulting error.
    # Learn why lists are unhashable.
    # Think of a suitable immutable alternative, such as a tuple.

#--------------------------------------------------------------------------------------------------------------------------------------------------


from functools import cache

@cache

def add(a):
    return a + a

num_list = [1,2,3,4,5,6,7,8,9]
print(add(num_list))


# ---------------------------------------------------
# complete Correct code

from functools import cache

@cache
def add(a):
    return sum(a)

# Tuple (works)
print(add((1, 2, 3)))
print(add((1, 2, 3)))

# List (gives error)
print(add([1, 2, 3]))

# ------------------------------------------------------------
# Create a decorator that prints a message before an addition function runs.

# Your function should accept two numbers and return their sum.

# Test with different numbers.
#--------------------------------------------------------------------------------------
def my_decorator(func):
    def wrapper(a, b):
        print("Addition function is about to run")
        return func(a, b)
    return wrapper


@my_decorator
def add_numbers(a, b):
    return a + b


print(add_numbers(5, 3))
print(add_numbers(10, 20))
print(add_numbers(7, 8))
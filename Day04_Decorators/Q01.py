# Create a decorator named my_decorator.

# It should print "Function is starting" before the original function runs.

# Create a function named greet() that prints "Hello, Python!".

# Apply your decorator to greet().
#------------------------------------------------------------------------------------------

def my_decoator(func):
    def wrapper():
        print('Function is starting')
        func()
    return wrapper

@my_decoator
def greet():
    print('Hello,Python!')

greet()
# Create a decorator that prints "Function executed" whenever the decorated function is called.

# Apply it to a function named say_hello().

# Call the function three times.
#-------------------------------------------------------

def my_decorator(func):
    def wrapper():
        print('Function executed')
        func()
    return wrapper
@my_decorator
def say_hello():
    print('Say Hello')

say_hello()
say_hello()
say_hello()
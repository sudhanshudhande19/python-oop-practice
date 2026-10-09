# Create a decorator that calls a function returning a string and prints the returned string in uppercase.

# Test it with a function returning "python oop practice".
#--------------------------------------------------------------------------------------------------------------------------
def my_decorator(func):
    def wrapper():
        result = func()          # Call the original function
        print(result.upper())    # Print the returned string in uppercase
    return wrapper


@my_decorator
def get_text():
    return "python oop practice"


get_text()
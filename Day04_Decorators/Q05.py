# Create a decorator that prints the name of the function being called.

# Test it with two different functions.
#-------------------------------------------------------------------------------------
def show_function_name(func):
    def wrapper():
        print("Function name:", func.__name__)
        func()
    return wrapper


@show_function_name
def greet():
    print("Hello!")


@show_function_name
def goodbye():
    print("Goodbye!")


greet()
goodbye()
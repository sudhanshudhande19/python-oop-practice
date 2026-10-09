# Create a decorator that works with functions accepting different numbers of positional and keyword arguments.

# Use *args and **kwargs in the wrapper.

# Test it with:

# A function accepting two numbers
# A function accepting a name and city
#-------------------------------------------------------------------------------------------------------------------------------

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper


# Function accepting two numbers
@my_decorator
def add(a, b):
    print("Sum =", a + b)


# Function accepting a name and city
@my_decorator
def introduce(name, city):
    print(f"My name is {name} and I live in {city}")


# Test cases
add(10, 20)

introduce(name="Sudhanshu", city="Nagpur")
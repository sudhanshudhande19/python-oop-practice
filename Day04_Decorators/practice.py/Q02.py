# Create a decorator that prints:

# "Before function"
# Executes the original function
# "After function"

# Test it using a function named welcome().
#-----------------------------------------------------

def my_decotator(fun):
    def wrapper():
        print('Before Function')
        fun()
        print('After Function')
    return wrapper

@my_decotator
def welcome():
    print('Welcome')

welcome()

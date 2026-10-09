# Create a decorator that executes a function three times whenever it is called once.

# Test it with a function that prints "Practice makes progress".
# ------------------------------------------------------------------------------------------------------------
def repeat_three_times(func):
    def wrapper():
        for i in range(3):
            func()
    return wrapper


@repeat_three_times
def practice():
    print("Practice makes progress")


practice()
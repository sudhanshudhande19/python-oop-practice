# Create a decorator that checks whether a function's number argument is positive.

# If the number is positive, execute the function. Otherwise, print "Number must be positive".

# Test with positive, zero, and negative values.
# -------------------------------------------------------------------------------------------------------------
def positive_number_required(func):
    def wrapper(num):
        if num > 0:
            func(num)
        else:
            print("Number must be positive")
    return wrapper


@positive_number_required
def show_number(num):
    print("Number is:", num)


# Test cases
show_number(10)   # Positive
show_number(0)    # Zero
show_number(-5)   # Negative
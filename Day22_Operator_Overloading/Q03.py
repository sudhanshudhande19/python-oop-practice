# Create a Number class and overload *.

# Requirements:

    # Store a numeric value.
    # Define __mul__().
    # Multiply two object values.
    # Return the result.
    # Test with different numbers.

#----------------------------------------------------------------------------------------------

class Number:

    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value

num = Number(5)
num2 = Number(5)

sum = num * num2

print(f'Sum = {sum}')
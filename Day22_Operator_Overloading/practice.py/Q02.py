# Create a Calculator class and overload the - operator.

# Requirements:

    # Store a number in each object.
    # Define __sub__().
    # Subtract the second object's value from the first.
    # Return the result.
    # Test with positive and negative results.

#--------------------------------------------------------------------------------------------------------


class Calculator:

    def __init__(self,value):
        self.value = value

    def __sub__(self, other):
        return self.value - other.value


# Positive result
num1 = Calculator(10)
num2 = Calculator(5)

result1 = num1 - num2
print(f"Positive Result = {result1}")

# Negative result
num3 = Calculator(5)
num4 = Calculator(10)

result2 = num3 - num4
print(f"Negative Result = {result2}")
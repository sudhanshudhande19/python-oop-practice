# Create a Number class and overload /.

# Requirements:

    # Store a number in each object.
    # Define __truediv__().
    # Divide the first object's value by the second.
    # Handle division by zero.
    # Return the result.

#--------------------------------------------------------------------------------------------------------------------------------------


class Number:
    def __init__(self,number):
        self.number = number

    def __truediv__(self, other):
        if other.number == 0:
                return "Error: Division by zero is not allowed"
        return self.number / other.number


num1 = Number(5)
num2 = Number(2)
total = num1 / num2
print(f'Total = {total}')

num3 = Number(5)
num4 = Number(0)
total = num3 / num4
print(f"Total = {total}")
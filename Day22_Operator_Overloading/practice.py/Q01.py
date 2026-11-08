# Create a Number class and overload the + operator.

# Requirements:

    # Create a class named Number.
    # Add a constructor that accepts one numeric value.
    # Create an __add__() method.
    # Accept another Number object as an argument.
    # Return the sum of both values.
    # Create two objects and add them using +.

#------------------------------------------------------------------------------------------------------------

class number:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

num1 = number(5)
num2 = number(5)

result = num1 + num2

print('Result = ',result)
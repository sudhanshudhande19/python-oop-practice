# Create a Calculator class with these static methods:
    # add(a, b)
    # subtract(a, b)
    # multiply(a, b)
    # divide(a, b)

# Requirements:

    # Each method returns its result.
    # Handle division by zero.
    # Call the methods using the class name.

#-------------------------------------------------------------------------------------------


class Calculator:
    @staticmethod
    def add(a,b):
        return f'{a} + {b} = {a+b}'
    
    @staticmethod
    def subtract(a,b):
        return f'{a} - {b} = {a-b}'
    @staticmethod
    def multiply(a,b):
        return f'{a} * {b} = {a*b}'

    @staticmethod
    def divide(a,b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        else:
            return f'{a} / {b} = {a/b}'

r = Calculator.add(8,9)
print(r)

r = Calculator.subtract(8,9)
print(r)

r = Calculator.multiply(8,9)
print(r)

r = Calculator.divide(8,9)
print(r)

r = Calculator.divide(8,0)
print(r)
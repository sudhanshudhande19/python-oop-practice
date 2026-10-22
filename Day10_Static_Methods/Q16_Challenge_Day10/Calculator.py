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
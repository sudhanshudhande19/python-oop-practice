# Create a Calculator class with static methods for addition, subtraction, multiplication, and division.

#----------------------------------------------------------------------------------------------------------------------

class Calculator:

    @staticmethod
    def all(number):
        if number > 0:
            print(f'Addition = {number +number}')
            print(f'Subtration = {number - number}')
            print(f'multiplication = {number * number}')
            print(f'Division = {number / number}')
        else:
            print(f'Invalid number')

s = Calculator.all(5)
d = Calculator.all(0)
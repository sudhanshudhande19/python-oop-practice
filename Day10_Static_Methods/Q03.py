# Create a Calculator class with a static method square(number).

# Return the square of a number.

# Test positive, negative, and zero values.

#----------------------------------------------------------------------------------------------------


class Calculator:
    @ staticmethod
    def square(number):
        if number > 0:
            print('Positive')
            return f'{number} Square = {number * number}'
        elif number == 0:
            return 'Zero'
        else:
            return 'Negative'

r = Calculator.square(2)
print(r)
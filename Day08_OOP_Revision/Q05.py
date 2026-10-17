# Create a Calculator class with a static method is_even(number).

# Requirements:
    # Return True if the number is even.
    # Return False if the number is odd.
    # Test at least five different numbers.

# Use @staticmethod

class Calculator:
    def is_even(number):
        if number %2 == 0:
            print('True')
        else:
            print('False')

e = Calculator()
e.is_even(5)
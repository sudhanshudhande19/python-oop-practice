# Create a Calculator class with a static method is_even(number).

# Requirements:
    # Return True if the number is even.
    # Return False if the number is odd.
    # Test at least five different numbers.

# Use @staticmethod

class Calculator:
    @staticmethod
    def is_even(number):
        return number % 2 == 0


e = Calculator()

print(e.is_even(2))
print(e.is_even(5))
print(e.is_even(10))
print(e.is_even(13))
print(e.is_even(24))
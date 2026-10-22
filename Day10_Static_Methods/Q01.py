# Create a NumberChecker class.

# Create a static method is_even(number) that returns True if the number is even and False otherwise.

# Test at least five numbers.

#--------------------------------------------------------------------------------------------------------------------------------------------------------


class NumberChecker:
    @staticmethod
    def is_even(number):
        if number %2 == 0:
            return True
        else:
            return False

r = NumberChecker.is_even(5)
print(r)
r = NumberChecker.is_even(2)
print(r)
r = NumberChecker.is_even(3)
print(r)
r = NumberChecker.is_even(9)
print(r)
r = NumberChecker.is_even(1)
print(r)
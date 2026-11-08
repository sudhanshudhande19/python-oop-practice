# Create a Fraction class and overload +.

# Requirements:

    # Store numerator and denominator.
    # Define __add__().
    # Add two fractions correctly.
    # Calculate a common denominator.
    # Return a new Fraction object.
    # Handle a zero denominator during initialization.
#---------------------------------------------------------------------------------------\

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        num = (self.numerator * other.denominator) + \
              (other.numerator * self.denominator)

        den = self.denominator * other.denominator

        return Fraction(num, den)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)

result = f1 + f2

print(result)
# Create a Rectangle class with:

    # length
    # width

# Requirements:

    # Create a class method from_string(data).
    # Accept input in the format "10,5".
    # Convert both values to numbers.
    # Calculate and display the area and perimeter.
    # Reject zero or negative dimensions.

#------------------------------------------------------------------------------------------------------------------


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def from_string(cls, data):
        length, width = map(int, data.split(','))

        if length <= 0 or width <= 0:
            raise ValueError("Dimensions must be positive numbers")

        return cls(length, width)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


try:
    r = Rectangle.from_string("10,5")

    print(f"Area = {r.area()}")
    print(f"Perimeter = {r.perimeter()}")

except ValueError as e:
    print(e)
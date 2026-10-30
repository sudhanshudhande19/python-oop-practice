# Create a Temperature class with a value stored in Celsius.

# Requirements:

    # Create a regular constructor that accepts Celsius.
    # Create a class method from_fahrenheit(value).
    # Convert Fahrenheit to Celsius before creating the object.
    # Create a method to display Celsius and Fahrenheit values.
    # Test different temperatures.

#---------------------------------------------------------------------------------------------------------------------


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, value):
        celsius = (value - 32) * 5 / 9
        return cls(celsius)

    def display(self):
        fahrenheit = (self.celsius * 9 / 5) + 32
        print(f"Celsius: {self.celsius:.2f}°C")
        print(f"Fahrenheit: {fahrenheit:.2f}°F")
        print("-" * 25)





t1 = Temperature(25)
t1.display()

t2 = Temperature.from_fahrenheit(77)
t2.display()

t3 = Temperature.from_fahrenheit(32)
t3.display()

t4 = Temperature(-40)
t4.display()
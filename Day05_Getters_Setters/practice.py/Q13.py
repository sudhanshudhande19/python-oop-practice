# Create a Temperature class with _celsius.
# Requirements:

    # Use a getter and setter for Celsius.
    # Reject temperatures below absolute zero: -273.15°C.
    # Create a read-only Fahrenheit property.

# Formula:
    # Fahrenheit = (Celsius × 9/5) + 32
# Test multiple temperature values.
#-----------------------------------------------------------------------------

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, new_celsius):
        if new_celsius >= -273.15:
            self._celsius = new_celsius
        else:
            print("Invalid Temperature! Below absolute zero.")

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32


# Create objects and test different temperatures
t1 = Temperature(25)
t2 = Temperature(0)
t3 = Temperature(-273.15)

print("Celsius:", t1.celsius)
print("Fahrenheit:", t1.fahrenheit)

print("Celsius:", t2.celsius)
print("Fahrenheit:", t2.fahrenheit)

print("Celsius:", t3.celsius)
print("Fahrenheit:", t3.fahrenheit)

# Test invalid temperature
t1.celsius = -300

print("Current Celsius:", t1.celsius)
print("Current Fahrenheit:", t1.fahrenheit)

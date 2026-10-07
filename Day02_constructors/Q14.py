# Create a Temperature class with:
# celsius

# Create methods:
# to_fahrenheit()
# to_kelvin()

# Formulas:
# Fahrenheit = (Celsius × 9/5) + 32
# Kelvin = Celsius + 273.15

# Create two different temperature objects and compare their results
#----------------------------------------------------------------------------------------

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def info(self):
        print(f"Celsius    : {self.celsius}°C")
        print(f"Fahrenheit : {self.to_fahrenheit():.2f}°F")
        print(f"Kelvin     : {self.to_kelvin():.2f} K")
        print("-" * 30)


temp1 = Temperature(25)
temp2 = Temperature(40)

temp1.info()
temp2.info()

# Comparison
if temp1.celsius > temp2.celsius:
    print(f"{temp1.celsius}°C is hotter than {temp2.celsius}°C")
elif temp1.celsius < temp2.celsius:
    print(f"{temp2.celsius}°C is hotter than {temp1.celsius}°C")
else:
    print("Both temperatures are equal.")
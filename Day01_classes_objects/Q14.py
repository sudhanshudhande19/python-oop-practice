# Create a Temperature class with:
# 1.celsius

# Create methods:
# 1.to_fahrenheit()
# 2.to_kelvin()

# Formulas:
# 1.Fahrenheit = (Celsius × 9/5) + 32
# 2.Kelvin = Celsius + 273.15
#------------------------------------------------------------

class Temperature:
    celsius = 00

    def to_fahrenheit(self):
        return (self.celsius * 9/5) +32

    def to_kelvin(self):
        return self.celsius + 273.15

    def info(self):
        print(f'Fahrenheit ={self.to_fahrenheit()}\nKelvin ={self.to_kelvin()}')

obj =Temperature()

obj.celsius = 25

obj.to_fahrenheit()
obj.to_kelvin()
obj.info()

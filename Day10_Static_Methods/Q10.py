# Create a TemperatureConverter class with these static methods:

    # celsius_to_fahrenheit(celsius)
    # fahrenheit_to_celsius(fahrenheit)

# Formulas:

    # Fahrenheit = (Celsius × 9/5) + 32
    # Celsius = (Fahrenheit − 32) × 5/9

# Test both conversions.

#-----------------------------------------------------------------------------------------------------


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5 ) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

r=  TemperatureConverter.celsius_to_fahrenheit(12)
print('celsius =',r)

r=  TemperatureConverter.fahrenheit_to_celsius(12)
print('fahrenheit =',r)
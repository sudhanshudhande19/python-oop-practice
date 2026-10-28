# Create a Temperature class.

# Requirements:

    # Create a static method celsius_to_fahrenheit(celsius).
    # Create a static method fahrenheit_to_celsius(fahrenheit).
    # Create a class method display_unit() that displays the class's default temperature unit.
    # Test all three methods
#-------------------------------------------------------------------------------------------------------------------------------

class Temperature:
    default_unit = "Celsius"
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @classmethod
    def displya_unit(cls):
        print(f"Default Temperature Unit = {cls.default_unit}")

print("25°C to Fahrenheit =", Temperature.celsius_to_fahrenheit(25))

print("98.6°F to Celsius =", Temperature.fahrenheit_to_celsius(98.6))

Temperature.displya_unit()
# Create a Temperature class.

# Requirements:

    # Store temperature in Celsius.
    # Implement __str__().
    # Implement __add__() to add a numeric temperature change.
    # Implement __lt__() to compare two temperatures.
    # Return new objects when adding temperatures.



#--------------------------------------------------------------------------------------------------------


class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    def __add__(self, change):
        return Temperature(self.celsius + change)

    def __lt__(self, other):
        return self.celsius < other.celsius


t1 = Temperature(25)
t2 = Temperature(30)

print(t1)          # 25°C
print(t1 + 5)      # 30°C
print(t1 < t2)     # True
# Create a Distance class and overload +.

# Requirements:

    # Store distance in kilometers and meters.
    # Define __add__().
    # Add two distance objects.
    # Convert excess meters into kilometers.
    # Return a new Distance object.
    # Display the final normalized distance.

#-----------------------------------------------------------------------------------

class Distance:
    def __init__(self, km, m):
        self.km = km
        self.m = m

    def __add__(self, other):
        new_km = self.km + other.km
        new_m = self.m + other.m

        new_km += new_m // 1000
        new_m = new_m % 1000

        return Distance(new_km, new_m)

    def __str__(self):
        return f"{self.km} km {self.m} m"


d1 = Distance(2, 500)
d2 = Distance(3, 800)

result = d1 + d2

print(result)
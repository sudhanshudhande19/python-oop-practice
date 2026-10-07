#Create a Circle class.
# The constructor should accept:
# radius

# Create methods:
# area()
# circumference()

# Use:
#Area = π × r²
# Circumference = 2 × π × r
#--------------------------------------------------------

class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

    def info(self):
        print(f'Area Of Circle = {self.area()}\nCirumaference = {self.circumference()}')

obj = circle(12)
obj.info()
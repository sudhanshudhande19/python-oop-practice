# Create a Circle class with radius. Calculate area and circumference.

#----------------------------------------------------------------------------------------------\


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(f'Area = {3.14  * self.radius * self.radius}')\

    def circumference(self):
        print(f'circumference  = {2 * 3.14 * self.radius}')

s = Circle(5)
s.area()
s.circumference()
# Concept: Hierarchical Inheritance with mathematical calculations.

# Requirements:

    # Create Shape as parent class.
    # Create Circle, Rectangle, and Triangle child classes.
    # Circle stores radius.
    # Rectangle stores length and width.
    # Triangle stores base and height.
    # Calculate the area of each shape.
    # Display all three areas.


#----------------------------------------------------------------------------------------------------------------------


class circle:

    def __init__(self,radius):
        self.radius = radius

class Ractangle(circle):

    def __init__(self, radius,length,width):
        super().__init__(radius)
        self.length = length
        self.width = width

class triangle(circle):

    def __init__(self, radius,base,height):
        super().__init__(radius)
        self.base = base
        self.height = height



r = Ractangle(7,10,5)
print(f'Circle Area = {3.14 *r.radius * r.radius}')
print(f'Rectangle Area = {r.length * r.width}')

t = triangle(7,8,6)
print(f'Triangle Area = {t.base * t.height * 1/2}')
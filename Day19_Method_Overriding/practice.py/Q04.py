# Create a parent class Shape with an area() method. Override it in Circle.

#--------------------------------------------------------------------------------------------

class Shape:
    def area(self):
        print("Area of Shape")


class Circle(Shape):
    def area(self):
        print("Area of Circle = πr²")

s = Shape()
c = Circle()
s.area()
c.area()
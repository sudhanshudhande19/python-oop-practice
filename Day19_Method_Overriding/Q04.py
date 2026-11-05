# Create a parent class Shape with an area() method. Override it in Circle.

#--------------------------------------------------------------------------------------------

class Shape:
    def area(self):
        print("Area of Shape")


class Circle(Shape):
    def area(self):
        print("Area of Circle = πr²")


c = Circle()
c.area()
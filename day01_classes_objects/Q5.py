# Create a Rectangle class with (length ,width )Create a method area() that returns the area of the rectangle.

class Rectangle:
    length = 20
    width = 5

    def area(self):
        print(f'Area of Rectangle ={self.length * self.width}')

obj = Rectangle()
obj.area()

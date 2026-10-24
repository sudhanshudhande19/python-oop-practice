# Create a Rectangle class with length and width.

# Methods:

    # calculate_area()
    # calculate_perimeter()
    # Reject zero or negative dimensions.

#----------------------------------------------------------------------------------------------

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_area(self):
        if self.length <= 0 and self.width <= 0:
            print('Reject The Dimension')
        else:
            print(f'Area of Reactangle =  {self.length * self.width}')

    def calculate_perimeter(self):
        if self.length <= 0 and self.width <= 0:
            print('Reject The Dimension')
        else:
            print(f'Perimeter = {2* (self.length +  self.width)}')

e1 = Rectangle(6,4)
e1.calculate_area()
e1.calculate_perimeter()
print('---------------------')
e2 = Rectangle(0,0)
e2.calculate_area()
e2.calculate_perimeter()

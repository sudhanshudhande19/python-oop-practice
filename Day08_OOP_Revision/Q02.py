# Create a Rectangle class with:
    # length
    # width

# Methods:
    # area()
    # perimeter()

# Formulas:
    # Area = length × width
    # Perimeter = 2 × (length + width)

# Create two rectangle objects and calculate their area and perimeter.

#------------------------------------------------------------------------------------------
class rectangle:
    def __init__(self,length,width):
        self.length = length 
        self.width = width


    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

e1 = rectangle(22,12)
e2 = rectangle(32,15)

print('Area =',e1.area())
print('Perimeter  =',e1.perimeter())

print('Area =',e2.area())
print('Perimeter  =',e2.perimeter())
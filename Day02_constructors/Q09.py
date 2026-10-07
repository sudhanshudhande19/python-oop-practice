# Create a Rectangle class.
# The constructor should accept:
# 1.length
# 2.width

# Create methods:
# 1.area()
# 2.perimeter()

# Formulas:
# 1.Area = length × width
# 2.Perimeter = 2 × (length + width)
#------------------------------------------------------------------

class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 *(self.length + self.width)

    def info(self):
        print(f'Area of Rectangle ={self.area()}\nPerimeter = {self.perimeter()}')

obj = rectangle(20,5)
obj.info()

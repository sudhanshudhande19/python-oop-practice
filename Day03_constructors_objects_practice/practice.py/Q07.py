# Create a Rectangle class with:
# length
# width

# Create a method:
# area()

# Create two rectangle objects.
# Compare their areas and display which rectangle has the larger area.
#---------------------------------------------------------------------------------
class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width  = width

    def area(self):
        return self.length * self.width

    def info(self):
        print(f'Area of Rectangle ={self.area()}\n')
        print('--------------------------------------')
obj = rectangle(20,5)
obj2 = rectangle(10,15)


obj.info()
obj2.info()

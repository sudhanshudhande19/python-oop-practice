# Create a parent class Shape with a method description() that prints "This is a shape".

# Create a child class Rectangle with:
    # length
    # width
    # area()

# Display the description and calculate the rectangle's area.
#---------------------------------------------------------------------------------------------------------

class shape:
    def description(self):
        print('This is a shape')

class rectangle(shape):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        print(f'Area Reactangle ={self.length * self.width}')

print('--------------------------')
e1 = rectangle(12,10)
e1.description()
e1.area()
print('--------------------------')
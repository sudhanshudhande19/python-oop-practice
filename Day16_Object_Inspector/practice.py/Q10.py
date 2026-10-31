# Create a Product class and inspect its object using dir().

# Find these special methods:

# __init__
# __str__
# __class__
# __dict__

#------------------------------------------------------------------------------------------


class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def show(self):
        print(f'Name = {self.name}')
        print(f'Price = {self.price}')

e = Product('TV',50000)
e.show()

print(dir(e))
print(e.__init__)
print(e.__str__)
print(e.__class__)
print(e.__dict__)
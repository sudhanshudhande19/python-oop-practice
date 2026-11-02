# Create a Product class with:

    # name
    # price

# Create an Electronics class with:

    # warranty

# Use super() and display all details.

#-------------------------------------------------------------------------------------------

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price


class Electronics(Product):
    def __init__(self, name, price,warranty):
        super().__init__(name, price)
        self.warranty = warranty

e = Electronics('TV',50000,2)
print(f'Name = {e.name}')
print(f'Price = {e.price}')
print(f'Warranty = {e.warranty}')
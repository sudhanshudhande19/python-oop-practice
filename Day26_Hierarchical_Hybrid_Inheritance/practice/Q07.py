# Concept: Real-world product hierarchy.

# Requirements:

    # Create Product parent class.
    # Create three child classes.
    # Product stores name and price.
    # Electronics stores warranty.
    # Clothing stores size.
    # Furniture stores material.
    # Display the details of all products.

#---------------------------------------------------------------------------------------------------------------


class Product:

    def __init__(self,name,price):
        self.name = name 
        self.price = price

class Electronics(Product):

    def __init__(self, name, price,warranty):
        super().__init__(name, price)
        self.warranty = warranty

class clothing(Product):

    def __init__(self,name,price,size):
        super().__init__(name, price)
        self.size = size

class Furniture(Product):

    def __init__(self, name, price,material):
        super().__init__(name, price)
        self.material = material

a = Electronics('Laptop',55000,2)
b = clothing('shirt',800,'L')
c = Furniture('Table',5000,'Wood')

print(f'{a.name} : {a.price}, Warranty = {a.warranty} Year')
print(f'{b.name} : {b.price}, size = {b.size}')
print(f'{c.name} : {c.price}, Materical = {c.material}')
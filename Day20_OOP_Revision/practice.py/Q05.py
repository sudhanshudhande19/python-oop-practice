# Create a Product class with name, price, and quantity. Calculate total price.

#-------------------------------------------------------------------------------------------------------

class Product:

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


s = Product('TV',50500,3)
print(f'Name = {s.name}')
print(f'Price = {s.price}')
print(f'Quantity = {s.quantity}')
print(f'Total Price = {s.price * s.quantity}')

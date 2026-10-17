# Create a Product class with:
    # name
    # price
    # quantity

# Requirements:

    # Reject a negative price or quantity.
    # Create a method total_price().
    # Update the quantity and calculate the new total.
# Formula: Total price = price × quantity.
#---------------------------------------------------------------------------------------------

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price  = price
        self.quantity = quantity

    def total_price(self):
        if self.price < 0:
            print('REJECT THE NEGATIVE PRICE')
        else:
            print(f'total price = {self.price * self.quantity}')


e = Product('TV',55000,3)
print('Name =',e.name)
print('Price = ',e.price)
print('Quantity =',e.quantity)
e.total_price()

# reate a Product class with:

    # product_name
    # price
    # quantity

# Requirements:

    # Create a class method from_string(data).
    # Accept data in the format "Laptop,55000,2".
    # Convert price and quantity into numeric values.
    # Calculate the total price.

#------------------------------------------------------------------------------------------------

class Product:

    def __init__(self,product_name,price,quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    @classmethod
    def from_string(cls,data):
        name ,price,quantity = data.split(',')
        return cls(name ,int(price),int(quantity))


pro = Product.from_string('Laptop,55000,2')
print(f'Product Name = {pro.product_name}\nPrice = {pro.price}\nQuantity = {pro.quantity}')

print(f'Total Price = {pro.price * pro.quantity}')
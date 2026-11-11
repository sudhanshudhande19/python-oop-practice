# Concept: Multilevel Inheritance with product details.

# Requirements:

    # Create Product, Electronics, and Laptop classes.
    # Product stores product name and price.
    # Electronics stores warranty period.
    # Laptop stores RAM and storage.
    # Display all product details.

#-----------------------------------------------------------------------------------------------------------------


class Product:

    def __init__(self,product_name,price):
        self.product_name = product_name
        self.price = price 

class Electronics(Product):

    def __init__(self, product_name, price,warranty):
        super().__init__(product_name, price)
        self.warranty = warranty

class laptop(Electronics):

    def __init__(self, product_name, price, warranty,Ram,Storage):
        super().__init__(product_name, price, warranty)
        self.Ram = Ram
        self.Storage = Storage

    def details(self):
        print(f'Product Name = {self.product_name}')
        print(f'Price = {self.price}')
        print(f'Warranty = {self.warranty} Years')
        print(f'RAM = {self.Ram} GB')
        print(f'Storage = {self.Storage} GB SSD')

s = laptop('Laptop',55000,2,16,512)
s.details()
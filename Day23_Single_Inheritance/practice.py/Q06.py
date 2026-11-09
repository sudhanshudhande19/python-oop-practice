# Create a Product parent class and an Electronics child class.

# Concept: Inheritance with Multiple Attributes.

# Requirements:

    # Parent stores product name and price.
    # Child stores warranty period and brand.
    # Use super() to initialize parent attributes.
    # Create a method to display complete product details

#-------------------------------------------------------------------------------------------------


class Product:
    def __init__(self,name,price):
        self.name = name 
        self.price = price


class Electronics(Product):
    def __init__(self, name, price,warranty,brand):
        super().__init__(name, price)
        self.warranty = warranty
        self.brand = brand

    def display(self):
        print(f'Product Name = {self.name}')
        print(f'Price = {self.price}')
        print(f'Warranty = {self.warranty}')
        print(f'Brand = {self.brand}')

pro = Electronics('TV',50000,2,'Samsung')
pro.display()

# Create a Product class with:

    # name
    # price

# Create an ElectronicProduct class with:

    # warranty
    # calculate_discount()

# Use super() to initialize product information.

#-------------------------------------------------------------------------------------------------------------


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class ElectroniProduct(Product):
    def __init__(self, name, price,warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def calculate_discount(self):
        skk = self.price *(20 / 100)
        print(f'Discount Price = { self.price -skk}')

e = ElectroniProduct('TV',1000,2)

print(f'Name = {e.name}')
print(f'Price  = {e.price}')
print(f'Warranty = {e.warranty}')
e.calculate_discount()
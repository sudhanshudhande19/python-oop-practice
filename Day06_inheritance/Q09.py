# Create a parent class Product with:
    # name
    # price
    # display_product()

# Create a child class ElectronicProduct with:
    # brand
    # warranty_years

# Display all product information.
#-----------------------------------------------------------------------------

class product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def display_product(self):
        print(f'Name ={self.name}\nPrice ={self.price}')


class electrnicproduct(product):
    def __init__(self, name, price,brand,warranty_years):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_years = warranty_years


e1 = electrnicproduct('Laptop',75000,'Asus',1)

e1.display_product()
print('Brand =',e1.brand)
print('Warranty years =',e1.warranty_years)
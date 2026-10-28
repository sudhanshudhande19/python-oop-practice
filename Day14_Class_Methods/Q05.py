# Create a Product class with:

    # Class variable: tax_rate = 18
    # Instance variables: name, price

# Requirements:

    # Create a class method change_tax_rate(new_rate).
    # Update the tax rate for the entire class.
    # Display the current tax rate.
    # Calculate the tax amount for a product using its price and the current tax rate.

#--------------------------------------------------------------------------------------------------------------------------------------------------


class Product:
    tax_rate = 18

    def __init__(self,name,price):
        self.name = name
        self.price = price


    @classmethod
    def change_tax_rate(cle,new_rate):
        cle.tax_rate = new_rate
        print(f'Tax Rate = {cle.tax_rate}')

    def show(self):
        print(f'Name = {self.name}')
        print(f'Price = {self.price}')
        print(f'Total Amount = {(self.price * self.tax_rate) / 100}')

pro = Product('Laptop',50000)
Product.change_tax_rate(20)
pro.show()
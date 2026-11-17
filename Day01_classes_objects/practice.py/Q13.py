# Create a Product class with:

#1. name
#2. price
#3. quantity

# Create methods:
# 1.total_price()
# 2.discount()
# 3.final_price()

# Apply a 10% discount if the total price is greater than ₹5000.
#-----------------------------------------------------------------------------------

class Product:
    name = ''   # Class Attribute
    price = 00
    quantity = 00

    def total_price(self,):
        return self.price * self.quantity

    def discount(self):
        return self.total_price() *0.10


    def final_price(self):
        return self.total_price() - self.discount()
    
    def display(self):
        print(f"Product Name = {self.name}")
        print(f"Total Price = {self.total_price()}")
        print(f"Discount (10%) = {self.discount()}")
        print(f"Final Price = {self.final_price()}")
        print()

s1 = Product()
s2 = Product()
s3 = Product()

s1.name = 'Iphone Mobile'
s1.price = 150000
s1.quantity = 1

s2.name = 'Asusu Laptop'
s2.price = 225000
s2.quantity = 2

s3.name = 'Samsung Mobile'
s3.price = 140000
s3.quantity = 3

s1.display()
s2.display()
s3.display()
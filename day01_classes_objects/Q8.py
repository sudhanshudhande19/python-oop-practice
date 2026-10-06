# 8.Create a Product class with (name,price,quantity) Create three product objects. 
# Create a method: total_price() which returns: price × quantity

class Product:
    name = ''   # Class Attribute
    price = 00
    quantity = 00

    def total_price(self,):
        print(f'Product Name  ={self.name}\n{self.name} Total Price ={self.price *self.quantity}\n')


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

s1.total_price()
s2.total_price()
s3.total_price()

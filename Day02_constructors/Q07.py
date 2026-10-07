# Create a Product class with:

# 1.name
# 2.price
# 3.quantity

# Use the constructor to initialize the values.

# Create three products.
# Create a method:
# total_price()

# which calculates:
# price × quantity

# Display the total price of each product.
#-------------------------------------------------------------------

class product:
    def __init__(self,name,price,quantity):
        self.name  = name 
        self.price = price 
        self.quantity = quantity 

    def total_price(self):
        return self.price * self.quantity
    
    def info(self):
        print(f'Name ={self.name}\nTotal Price ={self.total_price()}\n')

obj =product('Laptop',150000,3)
obj2 = product('Samsung Phone',75000,2)
obj3 = product('Pen',90,5)

obj.info()
obj2.info()
obj3.info()
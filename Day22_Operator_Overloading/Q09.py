# Create a Product class and overload <.

# Requirements:

    # Store product name and price.
    # Define __lt__().
    # Compare two product prices.
    # Return a Boolean result.
    # Find the cheaper product.

#----------------------------------------------------------------------------------------


class Product:

    def __init__(self,name,price):
        self.name = name 
        self.price = price 

    def __It__(self,value):
        return self.price < value.price

pro = Product('TV',50000)
pro2 = Product('Mobile',22000)


s = [pro,pro2]

for i in s:
    print(f'Name = {i.name}')
    print(f'Price = {i.price}')
    print('--------------------------')
print(pro.price < pro2.price)
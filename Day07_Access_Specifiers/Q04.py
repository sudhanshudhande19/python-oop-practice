# Create a Product class with public attributes:

    # name
    # price
    # quantity

# Create a method total_price() that calculates the total cost.
# Access the attributes and call the method using an object.

#--------------------------------------------------------------------------

class product:
    def __init__(self,name,price,qunatity):
        self.name = name
        self.price = price
        self.qunatity = qunatity

    def total_price(self):
        print( f'Final Price = {self.price *self.qunatity}')

obj = product('TV',64000,3)

print('Name =',obj.name)
print('Price =',obj.price)
print('Qunatity =',obj.qunatity)
obj.total_price()
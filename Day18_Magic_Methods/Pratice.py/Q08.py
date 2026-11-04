# create a Product class with:

    # price
    # quantity

# Implement __mul__() to calculate the total cost when multiplying two compatible objects or a product by a supported numeric value. Clearly define the behavior you choose.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

    def __mul__(self, other):
        if isinstance(other, Product):
            return self.total_cost() * other.total_cost()

        elif isinstance(other, (int, float)):
            return self.total_cost() * other

        return NotImplemented


e = Product(55700, 2)

print(e * 1)      # 111400
print(e * 2)      # 222800

p2 = Product(100, 5)
print(e * p2)     # 111400 * 500 = 55700000
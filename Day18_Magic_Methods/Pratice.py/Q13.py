# Create a Product class.

# Requirements:

    # Store product name and price.
    # Implement __eq__().
    # Implement __lt__().
    # Compare products by price.

#---------------------------------------------------------------------


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price


e = Product("TV", 5000)
f = Product("Mobile", 15000)

print(f"Are both product prices equal? {e == f}")
print(f"Is TV cheaper than Mobile? {e < f}")
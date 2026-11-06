# Create a ShoppingCart class using __str__(), __len__(), __add__(), and __contains__().

# --------------------------------------------------------------------------------------------------------

class ShoppingCart:
    def __init__(self, items=None):
        self.items = items if items else []

    def __str__(self):
        return f"Shopping Cart: {', '.join(self.items)}"

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        return ShoppingCart(self.items + other.items)

    def __contains__(self, item):
        return item in self.items


cart1 = ShoppingCart(["Laptop", "Mouse"])
cart2 = ShoppingCart(["Keyboard", "Headphones"])

print(cart1)                  # __str__
print(len(cart1))             # __len__

cart3 = cart1 + cart2         # __add__
print(cart3)

print("Mouse" in cart1)       # __contains__
print("Monitor" in cart1)
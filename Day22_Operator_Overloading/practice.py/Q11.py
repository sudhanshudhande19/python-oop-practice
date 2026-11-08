# Create a ShoppingCart class and overload +.

# Requirements:

    # Store products in a list.
    # Store the total amount.
    # Define __add__().
    # Combine products from two carts.
    # Calculate the new total amount.
    # Return a new ShoppingCart object.
    # Do not modify the original carts.
#------------------------------------------------------------------------------------------------

class ShoppingCart:
    def __init__(self, product_list, price):
        self.product_list = product_list
        self.price = price

    def __add__(self, other):
        new_products = self.product_list + other.product_list
        new_price = self.price + other.price

        return ShoppingCart(new_products, new_price)

    def __str__(self):
        return f"Products: {self.product_list}\nTotal: {self.price}"


p = ShoppingCart(['TV', 'Mobile'], 50000)
j = ShoppingCart(['Keyboard', 'Headphones'], 5000)

s = p + j

print(s)
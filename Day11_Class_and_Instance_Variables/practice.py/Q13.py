# Create a ShoppingCart class.

# Requirements:

    # Each object should have its own items list.
    # Create two shopping cart objects.
    # Add different items to each cart.
    # Display both carts and ensure that their items remain separate.

# Important: Create the list inside __init__() so each object has its own list.

#----------------------------------------------------------------------------------------------------------------------------------------

class Shoppingcart:

    def __init__(self,item):
        self.item = item

e1 = Shoppingcart(['Shirt','Shoes','watch'])
e2 = Shoppingcart(['Laptop','Mouse','keyboard'])

print("Cart 1:", e1.item)
print("Cart 2:", e2.item)
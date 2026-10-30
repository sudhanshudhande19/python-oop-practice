# Create a ShoppingCart class.

# Requirements:

    # Store items separately for each cart.
    # Implement add_item(name, price, quantity).
    # Implement remove_item(name).
    # Implement calculate_total().
    # Reject invalid prices and quantities.
    # Create two cart objects and verify that their items do not mix.

#-------------------------------------------------------------------------------------------------------------------------------



class ShoppingCart:

    def __init__(self):
       
        self.items = []

    def add_item(self, name, price, quantity):

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name cannot be empty")

        if not isinstance(price, (int, float)) or isinstance(price, bool) or price <= 0:
            raise ValueError("Price must be greater than zero")

        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.items.append(item)
        print(f"{name} added to cart!")

    def remove_item(self, name):

        for item in self.items:
            if item["name"].lower() == name.lower():
                self.items.remove(item)
                print(f"{name} removed from cart!")
                return

        print(f"{name} not found in cart.")

    def calculate_total(self):

        total = 0

        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

    def display_cart(self):

        print("\nShopping Cart")
        print("-" * 35)

        if not self.items:
            print("Cart is empty")
            return

        for item in self.items:
            subtotal = item["price"] * item["quantity"]

            print(f"Name: {item['name']}")
            print(f"Price: ₹{item['price']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Subtotal: ₹{subtotal}")
            print("-" * 35)

        print(f"Total Amount: ₹{self.calculate_total()}")


# Create two separate cart objects
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Add items to Cart 1
cart1.add_item("Laptop", 50000, 1)
cart1.add_item("Mouse", 500, 2)

# Add items to Cart 2
cart2.add_item("Mobile", 20000, 1)
cart2.add_item("Keyboard", 1000, 1)

# Display both carts
print("\n===== CART 1 =====")
cart1.display_cart()

print("\n===== CART 2 =====")
cart2.display_cart()

# Remove an item from Cart 1
cart1.remove_item("Mouse")

print("\n===== CART 1 AFTER REMOVAL =====")
cart1.display_cart()

print("\n===== CART 2 CHECK =====")
cart2.display_cart()

# Test invalid input
try:
    cart1.add_item("Headphones", -500, 2)
except ValueError as error:
    print("Error:", error)

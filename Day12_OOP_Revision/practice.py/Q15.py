# Create a ShoppingCart class.

# Requirements:

    # Store items separately for each cart.
    # Implement add_item(name, price, quantity).
    # Implement remove_item(name).
    # Implement calculate_total().
    # Reject invalid prices and quantities.
    # Create two cart objects and verify that their items do not mix

#----------------------------------------------------------------------------------------------------------------------------



class ShoppingCart:
    def __init__(self):
        # Each cart gets its own list
        self.items = []

    def add_item(self, name, price, quantity):
        if price <= 0:
            print("Invalid price! Price must be positive.")
            return

        if quantity <= 0 or not isinstance(quantity, int):
            print("Invalid quantity! Quantity must be a positive integer.")
            return

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }

        self.items.append(item)
        print(f"{name} added to cart successfully.")

    def remove_item(self, name):
        for item in self.items:
            if item["name"].lower() == name.lower():
                self.items.remove(item)
                print(f"{name} removed from cart.")
                return

        print(f"{name} not found in cart.")

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["price"] * item["quantity"]

        return total

    def display_items(self):
        if not self.items:
            print("Cart is empty.")
            return

        for item in self.items:
            item_total = item["price"] * item["quantity"]
            print(
                f'{item["name"]}: ₹{item["price"]} '
                f'x {item["quantity"]} = ₹{item_total}'
            )

        print("Grand Total: ₹", self.calculate_total())


# Create two separate cart objects
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Add items to Cart 1
cart1.add_item("Shirt", 500, 2)
cart1.add_item("Shoes", 1200, 1)

print("\n--- Cart 1 ---")
cart1.display_items()

# Add items to Cart 2
cart2.add_item("Laptop", 50000, 1)
cart2.add_item("Mouse", 800, 2)

print("\n--- Cart 2 ---")
cart2.display_items()

# Remove an item from Cart 1
print("\nRemoving Shoes from Cart 1:")
cart1.remove_item("Shoes")

# Verify that carts remain separate
print("\n--- Cart 1 After Removal ---")
cart1.display_items()

print("\n--- Cart 2 Remains Unchanged ---")
cart2.display_items()

# Test invalid values
print("\n--- Validation Tests ---")
cart1.add_item("Pen", -10, 2)
cart1.add_item("Book", 100, 0)

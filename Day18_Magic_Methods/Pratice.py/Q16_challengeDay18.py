
class ShoppingCart:

    def __init__(self, customer_name, items=None):
        self.customer_name = customer_name
        self.items = items.copy() if items else []
        self.total_amount = self.calculate_total()

    def __str__(self):
        return (
            f"Customer: {self.customer_name}\n"
            f"Total Items: {len(self)}\n"
            f"Total Amount: ₹{self.total_amount}"
        )

    def __repr__(self):
        return f"ShoppingCart({self.customer_name!r}, {self.items!r})"

    def __len__(self):
        return len(self.items)

    def __contains__(self, product_name):
        return any(item["name"] == product_name for item in self.items)

    def __add__(self, other):
        if not isinstance(other, ShoppingCart):
            return NotImplemented

        new_items = self.items.copy() + other.items.copy()

        return ShoppingCart(
            self.customer_name + " & " + other.customer_name,
            new_items
        )

    def __lt__(self, other):
        if not isinstance(other, ShoppingCart):
            return NotImplemented

        return self.total_amount < other.total_amount

    def add_item(self, name, price):
        if not isinstance(name, str) or not name.strip():
            print("Invalid product name!")
            return

        if isinstance(price, bool) or not isinstance(price, (int, float)) or price <= 0:
            print("Invalid price!")
            return

        self.items.append({
            "name": name.strip(),
            "price": price
        })

        self.calculate_total()
        print(f"{name} added successfully!")

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                self.calculate_total()
                print(f"{name} removed successfully!")
                return

        print(f"{name} not found in cart!")

    def calculate_total(self):
        self.total_amount = sum(item["price"] for item in self.items)
        return self.total_amount

    def apply_discount(self, percentage):
        if isinstance(percentage, bool) or not isinstance(percentage, (int, float)) or not 0 <= percentage <= 100:
            print("Invalid discount!")
            return self.total_amount

        discount = self.total_amount * percentage / 100
        self.total_amount -= discount

        return self.total_amount

    def display_cart(self):
        print("\n===== SHOPPING CART =====")
        print(f"\nCustomer: {self.customer_name}")
        print("\nItems:")

        if not self.items:
            print("Cart is empty!")
        else:
            for item in self.items:
                print(f"{item['name']} - ₹{item['price']}")

        print(f"\nTotal Items: {len(self)}")
        print(f"Total Amount: ₹{self.total_amount}")


# Customer 1
cart1 = ShoppingCart("Rahul")

cart1.add_item("Shoes", 1200)
cart1.add_item("Watch", 1500)
cart1.add_item("Bag", 800)

cart1.display_cart()

print("\nIs Shoes Available?", "Shoes" in cart1)
print("Total Products:", len(cart1))


# Customer 2
cart2 = ShoppingCart("Aman")

cart2.add_item("Laptop", 50000)
cart2.add_item("Mouse", 800)

cart2.display_cart()


# Combine two carts
combined_cart = cart1 + cart2

print("\n===== COMBINED CART =====")
combined_cart.display_cart()


# Compare carts
print("\nIs Rahul's cart smaller than Aman's cart?", cart1 < cart2)


# Apply discount
cart1.apply_discount(10)

print("\n===== AFTER 10% DISCOUNT =====")
cart1.display_cart()


# Check original carts
print("\n===== ORIGINAL CARTS =====")
cart1.display_cart()
cart2.display_cart()

# Developer representation
print("\nREPR:", repr(cart1))

class Product:

    def __init__(self, product_name, price, quantity):
        if price < 0:
            raise ValueError("Price cannot be negative")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_name} - Rs. {self.price}"

    def __add__(self, other):
        if self.product_name == other.product_name:
            return Product(
                self.product_name,
                self.price,
                self.quantity + other.quantity
            )
        raise ValueError("Only same products can be combined")


class ShoppingCart:

    def __init__(self, customer_name, products=None):
        self.customer_name = customer_name
        self.products = products if products else []

        self.total_amount = sum(
            p.price * p.quantity for p in self.products
        )

    def __add__(self, other):
        new_products = self.products + other.products

        return ShoppingCart(
            self.customer_name,
            new_products
        )

    def __len__(self):
        return len(self.products)

    def __contains__(self, product_name):
        return any(
            p.product_name == product_name
            for p in self.products
        )

    def __str__(self):

        if not self.products:
            return (
                "===== E-COMMERCE SHOPPING CART =====\n\n"
                f"Customer: {self.customer_name}\n\n"
                "Cart is Empty"
            )

        result = "===== E-COMMERCE SHOPPING CART =====\n\n"
        result += f"Customer: {self.customer_name}\n\n"
        result += "Products:\n"

        for product in self.products:
            result += (
                f"{product.product_name} - Rs. "
                f"{product.price * product.quantity}\n"
            )

        result += f"\nTotal Amount: Rs. {self.total_amount}"

        return result


# Products
p1 = Product("Laptop", 50000, 1)
p2 = Product("Mouse", 500, 1)
p3 = Product("Keyboard", 1200, 1)

# Cart 1
cart1 = ShoppingCart(
    "Rahul",
    [p1, p2]
)

# Cart 2
cart2 = ShoppingCart(
    "Rahul",
    [p3]
)

# Combine carts
cart3 = cart1 + cart2

# Display cart
print(cart3)

# len()
print("Total Products:", len(cart3))

# in
print("Mouse in cart:", "Mouse" in cart3)
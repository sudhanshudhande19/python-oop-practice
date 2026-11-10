# Create ProductInfo and Inventory classes. Inherit both into an OnlineProduct class.

# Concept: Combining Product and Inventory Features.

# Requirements:

    # ProductInfo stores product name, price and category.
    # Inventory stores stock quantity and warehouse location.
    # OnlineProduct inherits both classes.
    # Add a method to calculate total stock value.
    # Add a method to check product availability.
    # Validate price and stock quantity.

#------------------------------------------------------------------------------------------------------

class ProductInfo:
    def __init__(self, name, price, category):
        self.name = name

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        self.price = price
        self.category = category


class Inventory:
    def __init__(self, quantity, warehouse_location):

        if quantity < 0:
            raise ValueError("Stock quantity cannot be negative")

        self.quantity = quantity
        self.warehouse_location = warehouse_location


class OnlineProduct(ProductInfo, Inventory):

    def __init__(self, name, price, category,quantity, warehouse_location):

        ProductInfo.__init__(self, name, price, category)
        Inventory.__init__(self, quantity, warehouse_location)

    def calculate_total_stock_value(self):
        return self.price * self.quantity

    def product_availability(self):
        if self.quantity > 0:
            return "Product is Available"
        return "Product is Not Available"



p = OnlineProduct(
    "TV",
    10000,
    "Electrical",
    120,
    "Nagpur"
)

print(f"Product Name = {p.name}")
print(f"Price = {p.price}")
print(f"Category = {p.category}")
print(f"Quantity = {p.quantity}")
print(f"Warehouse = {p.warehouse_location}")

print(f"Total Stock Value = {p.calculate_total_stock_value()}")
print(p.product_availability())
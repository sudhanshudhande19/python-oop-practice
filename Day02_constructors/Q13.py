# Create a Product class with:
# name
# price
# quantity

# Create methods:
# total_price()
# discount()
# final_price()

# Rules:
# Total > ₹5000 → 10% discount
# Total > ₹10000 → 20% discount
# Otherwise → No discount

# Display:
# Product Name
# Quantity
# Total Price
# Discount
# Final Price
#----------------------------------------------------
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def discount(self):
        total = self.total_price()

        if total > 10000:
            return total * 0.20
        elif total > 5000:
            return total * 0.10
        else:
            return 0

    def final_price(self):
        return self.total_price() - self.discount()

    def info(self):
        print(f"Product Name : {self.name}")
        print(f"Quantity     : {self.quantity}")
        print(f"Total Price  : ₹{self.total_price()}")
        print(f"Discount     : ₹{self.discount()}")
        print(f"Final Price  : ₹{self.final_price()}")
        print("-" * 30)


p1 = Product("Laptop", 3000, 2)
p2 = Product("Mobile", 6000, 2)
p3 = Product("Mouse", 500, 4)

p1.info()
p2.info()
p3.info()
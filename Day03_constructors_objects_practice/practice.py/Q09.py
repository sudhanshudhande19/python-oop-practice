# Create a Product class with:
# name
# price
# quantity

# Create methods:
# total_price()
# apply_discount()
# final_price()

# Discount rules:
# Total >= ₹10,000 → 20%
# Total >= ₹5,000  → 10%
# Otherwise        → 0%

# Display the complete bill.

#--------------------------------------------------------


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        if self.price >= 10000:
            return self.total_price() * 0.20
        elif self.price >= 5000:
            return self.total_price() * 0.10
        else:
            return 0

    def final_price(self):
        discount = self.apply_discount()
        final_amount = self.total_price() - discount

        print('---------Display the complete bill-----------')
        print(f"Name = {self.name}")
        print(f"Total Price = {self.total_price()}")
        print(f"Discount = {discount}")
        print(f"Final Price = {final_amount}")
        print("-" * 40)


obj1 = Product("Laptop", 150000, 3)
obj2 = Product("Samsung Phone", 75000, 2)
obj3 = Product("Pen", 90, 5)

obj1.final_price()
obj2.final_price()
obj3.final_price()
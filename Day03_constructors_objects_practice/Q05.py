# Create a Mobile class with:
# brand
# model
# price

# Create a method:
# apply_discount(percent)

# The method should calculate the discounted price.

# Create one mobile object and apply a discount.
#---------------------------------------------------------------

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, percent):
        discounted_price = self.price - (self.price * percent / 100)
        return discounted_price


# Create a mobile object
mobile1 = Mobile("Samsung", "Galaxy S24", 80000)

# Apply 10% discount
new_price = mobile1.apply_discount(10)

print("Brand:", mobile1.brand)
print("Model:", mobile1.model)
print("Original Price:", mobile1.price)
print("Price after 10% discount:", new_price)
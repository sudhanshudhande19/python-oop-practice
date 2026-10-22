# Create a ProductUtility class with static methods:

    # calculate_total(price, quantity)
    # apply_discount(price, percent)

# Requirements:

    # Reject negative prices and quantities.
    # Calculate the total cost.
    # Apply a valid discount percentage.
    # Test different products.

#-------------------------------------------------------------------------------------------

class ProductUtility:

    @staticmethod
    def calculate_total(price, quantity):
        if price < 0:
            return "Negative price is not allowed"

        if quantity < 0:
            return "Negative quantity is not allowed"

        return price * quantity

    @staticmethod
    def apply_discount(price, percent):
        if price < 0:
            return "Negative price is not allowed"

        if percent < 0 or percent > 100:
            return "Invalid discount percentage"

        discount = (price * percent) / 100
        return price - discount


# Testing different products

print("Product 1:")
print("Total =", ProductUtility.calculate_total(500, 3))
print("After Discount =", ProductUtility.apply_discount(500, 10))

print("\nProduct 2:")
print("Total =", ProductUtility.calculate_total(1200, 2))
print("After Discount =", ProductUtility.apply_discount(1200, 25))

print("\nProduct 3:")
print("Total =", ProductUtility.calculate_total(-100, 5))
print("After Discount =", ProductUtility.apply_discount(500, 120))
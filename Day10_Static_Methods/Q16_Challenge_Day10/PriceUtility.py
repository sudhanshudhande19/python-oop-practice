# Create these static methods:

    # calculate_discount(price, percent)
    # calculate_final_price(price, percent)

# Requirements:

    # Reject negative prices.
    # Accept percentages from 0 to 100.
    # Calculate the discount amount.
    # Calculate the final price after discount.
    # Test multiple products.

#-----------------------------------------------------------------------------------------

class ProductUtility:

    @staticmethod
    def calculate_discount(price, percent):
        if price < 0:
            return "Negative price is not allowed"

        if not (0 <= percent <= 100):
            return "Invalid discount percentage"

        return (price * percent) / 100

    @staticmethod
    def calculate_final_price(price, percent):
        discount = ProductUtility.calculate_discount(price, percent)

        if isinstance(discount, str):
            return discount

        return price - discount


# Test Product 1
price1 = 1000
percent1 = 10

print("Product 1")
print("Discount:", ProductUtility.calculate_discount(price1, percent1))
print("Final Price:", ProductUtility.calculate_final_price(price1, percent1))

print()

# Test Product 2
price2 = 2500
percent2 = 20

print("Product 2")
print("Discount:", ProductUtility.calculate_discount(price2, percent2))
print("Final Price:", ProductUtility.calculate_final_price(price2, percent2))

print()

# Test Product 3
price3 = 500
percent3 = 15

print("Product 3")
print("Discount:", ProductUtility.calculate_discount(price3, percent3))
print("Final Price:", ProductUtility.calculate_final_price(price3, percent3))
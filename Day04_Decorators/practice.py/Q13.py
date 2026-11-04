# Create a decorator for a product-price function.

# The decorator should apply a 10% discount to the price returned by the original function.

# Test it with at least two different product prices.
#---------------------------------------------------------------------------------------------------------
def apply_discount(func):
    def wrapper(*args, **kwargs):
        original_price = func(*args, **kwargs)
        discounted_price = original_price - (original_price * 0.10)
        return discounted_price
    return wrapper


@apply_discount
def get_price(price):
    return price


# Test cases
print("Product 1 Price After Discount:", get_price(1000))
print("Product 2 Price After Discount:", get_price(500))
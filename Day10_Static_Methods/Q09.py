# Create a PriceUtility class with a static method calculate_discount(price, percent).

# Requirements:
    # Calculate the discount amount.
    # Reject negative prices.
    # Accept a discount percentage between 0 and 100.
    # Return the final price after discount.

#-----------------------------------------------------------------------------------------------------------------------------

class PriceUtility:
    @staticmethod
    def calculate_discount(price,percent):
        if price < 0:
            print('InValid Price')
        elif price > 0:
            if 0 < percent < 100:
                discount = (price * percent) / 100
                return price - discount
            else:
                return 'Invalid Percent'

e = int(input('Enter The Price ='))
t = int(input('Enter The Discount ='))

r = PriceUtility.calculate_discount(e,t)
print('Final Price =',r)
    
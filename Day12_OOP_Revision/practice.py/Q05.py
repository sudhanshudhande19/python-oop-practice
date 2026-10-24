# Create a Product class with name and price.
# Create a method apply_discount(percent).

# Requirements:

    # Accept discounts from 0 to 100.
    # Reject negative prices.
    # Update the product price after applying the discount.
    # Display the final price.

#-------------------------------------------------------------------------------------------------

class Product:

    def __init__(self,name,price):
        self.name = name
        if price >= 0:
            self.price = price
        else:
            print('Reject The Price')

    def apply_discount(self,percent):
        if 0 <=  percent <= 100:
            discount = (self.price * percent)/ 100
            self.price = self.price - discount
            print(f'Name = {self.name}')
            print(f'final Price = {self.price}')
        else:
            print('Enter The Correct Discount')

e1 = Product('Tv',50000)
e1.apply_discount(25)

e2 = Product('Mobile',55000)
e2.apply_discount(10)

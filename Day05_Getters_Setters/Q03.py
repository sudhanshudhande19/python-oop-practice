# Create a Product class with _price.

    # Create a getter for the price.
    # Create a setter that accepts only prices greater than zero.
    # Test different prices.

#---------------------------------------------------------------------------------

class product:
    def __init__(self,with_price):
        self._with_price = with_price

    @property
    def with_price(self):
        return self._with_price

    @with_price.setter
    def with_price(self,new_price):
        self._with_price = new_price
        if new_price > 0:
            print('price =',new_price)
        else:
            print('Not Accept This Value')


obj = product(500)
print(obj.with_price)
obj.with_price = 1000
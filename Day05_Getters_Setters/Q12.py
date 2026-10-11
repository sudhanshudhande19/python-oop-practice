# Create a Product class with:
    # _name
    # _price
    # _quantity

# Requirements:
    # Price must be greater than zero.
    # Quantity cannot be negative.
    # Create a read-only property total_price.

# Formula:
    # Total Price = price × quantity
    # Try to read and calculate the total price for three products.

#-----------------------------------------------------------------------------
class product:
    def __init__(self,name,price,quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        self._name = new_name

    @property
    def price(self):
        return self.price
    @price.setter
    def price(self,new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print('Price Cannot be Zero')

    @property
    def qunatity(self):
        return self._quantity
    @qunatity.setter
    def qunatity(self,new_qunatity):
        if new_qunatity >= 0:
            self._quantity = new_qunatity
            
        else:
            print('Quantity Cannot Be Negative')

    @property
    def total_price(self):
        return self._price * self.qunatity

    def info (self): 
        print('name =',self._name)
        print('Price =',self._price)
        print('Quantity =',self._quantity)
        print('Total Price =',self.total_price)
        print('-----------------------------------')

obj = product('Laptop',1000000,3) 
obj2 = product('Mobile',25000,4)
obj3 = product('tv',750000,2)

obj.info()
obj2.info()
obj3.info()
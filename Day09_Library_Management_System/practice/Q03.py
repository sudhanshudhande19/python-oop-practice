# Create a Book class with:
    # title
    # price

# Requirements:
    # Create a method update_price(new_price).
    # Reject zero or negative prices.
    # Display the updated price

#----------------------------------------------------------------------------

class Book:
    def __init__(self,title,price):
        self.title  = title
        self.price = price

    def update_price(self,new_price):
        if 0 < new_price < 100:
            print('Reject the Price')
        else:
            print('Price = ',self.price)
            self.price = new_price
            print('Updated Price =',new_price)

e = Book('Java',500)
print('Title = ',e.title)
e.update_price(600)


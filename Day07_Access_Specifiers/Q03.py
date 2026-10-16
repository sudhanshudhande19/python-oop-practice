# Create a Car class with public attributes:
    # brand
    # model
    # price

# Access and update the price outside the class. Display the updated details.
#-------------------------------------------------------------------------------------------------------

class car:
    def __init__(self):
        self.brach = 'BMW'
        self.model = 2026
        self.price = 890990


obj = car()

print('Brach =',obj.brach)
print('Model =',obj.model)
obj.price = 975500
print('Price =',obj.price)
# Create a Car class with a constructor that accepts:

# 1.brand
# 2.model
# 3.price

# Create one object and display its details.
#----------------------------------------------------------------------------

class car:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def info(self):
        print(f'Brand ={self.brand}\nModel ={self.model}\nPrice = {self.price}')

obj = car('BMW',2025,850000)
obj.info()
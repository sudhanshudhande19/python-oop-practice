# Create a Mobile class with a constructor that accepts:

# 1.brand
# 2.model
# 3.price
# 4.storage

# Create one object and display all details.
#------------------------------------------------------------------------

class mobile:
    def __init__(self,brand,model,price,storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage

    def info(self):
        print(f'Brand ={self.brand}\nModel ={self.model}\nPrice ={self.price}\nStorage = {self.storage}')

obj = mobile('Samsung',2026,50000,'212GB')
obj.info()
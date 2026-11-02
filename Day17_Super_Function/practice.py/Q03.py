# Create a Vehicle class with:

    # brand
    # start()

# Create a Car class with:

    # model
    # display()

# Use super() to initialize the parent attributes.

#-------------------------------------------------------------------------------------------


class Vehical:
    def __init__(self,brand):
        self.brand = brand

    def start(self):
        print(f'Start Tha {self.brand} 1999 year')
class Car(Vehical):
    def __init__(self, brand,Model):
        super().__init__(brand)
        self.Model = Model 

    def display(self):
        print(f'Brand = {self.brand}')
        print(f'Model ={self.Model}')
        
e = Car('BMW',2023)
e.display()
e.start()
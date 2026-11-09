# Create a Vehicle class and inherit it into Car.

# Concept: Reusing Parent Attributes.

# Requirements:

    # Parent class stores brand and model.
    # Child class stores fuel type.
    # Create a method to display vehicle details.
    # Use super() in the child constructor.

#--------------------------------------------------------------------------------


class Vehical:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehical):

    def __init__(self, brand, model,fuel):
        super().__init__(brand, model)
        self.fuel = fuel

    def display(self):
        print(f'Brand = {self.brand}')
        print(f'Model = {self.model}')
        print(f'Fuel = {self.fuel}L')

s = Car('BMW',2025,15)
s.display()
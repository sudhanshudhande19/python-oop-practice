# Concept: Multilevel Inheritance with attributes.

# Requirements:

    # Create three classes: Vehicle, Car, ElectricCar.
    # Vehicle should store brand.
    # Car should store model.
    # ElectricCar should store battery capacity.
    # Display all details using an object of ElectricCar.

#-------------------------------------------------------------------------------------------------------

class vehical:

    def __init__(self,brand):
        self.brand = brand

class car(vehical):

    def __init__(self, brand,model):
        super().__init__(brand)
        self.model = model

class ElectricCar(car):

    def __init__(self, brand, model,battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

s = ElectricCar('Tesla','Model 3',75)
print(f'Brand ={s.brand}')
print(f'Model = {s.model}')
print(f'Battery = {s.battery_capacity} kwh')

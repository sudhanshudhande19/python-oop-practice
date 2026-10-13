# Create a parent class Vehicle with:
    # brand
    # speed
    # display_vehicle()

# Create a child class Car with:
    # model
    # display_car()

# Create a car object and display all details.
#--------------------------------------------------------------------
class vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def display_vehicle(self):
        print(f'Brand ={self.brand}\nSpeed ={self.speed}')

class car(vehicle):
    def __init__(self, brand, speed,model):
        super().__init__(brand, speed)
        self.model = model

    def display_car(self):
        print(f'Model ={self.model}')


print('----------------------')

e2 = car('KIYA',160,2025)
e2.display_vehicle()
e2.display_car()
print('----------------------')
# Create a parent class Vehicle with:

    # brand
    # _speed

# Create a child class Car.
# Add a method display_vehicle() that displays the brand and speed.
#--------------------------------------------------------------------------------------------------------

class Vehicle:
    def __init__(self,brand,speed):
        self.brand = brand
        self._speed = speed


class car(Vehicle):
    def display_vehicle(self):
        print(f'Brand ={self.brand}')
        print(f'Speed ={self._speed}')

obj = car('BMW',280)
obj.display_vehicle()
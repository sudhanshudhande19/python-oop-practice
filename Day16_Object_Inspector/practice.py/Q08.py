# Create a Car class with:

# brand
# model
# speed
# start()
# stop()

# Use dir() on both the class and its object.

#-----------------------------------------------------------------------------------------------


class Car:

    def __init__(self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def start(self):
       print(f'{self.brand} Brand is start 1999') 

    def stop(self):
        print(f'And this {self.brand} brand stop is 2026 year')

e = Car('BMW',2000,180)
print(f'Name = {e.brand}')
print(f'Model = {e.model}')
print(f'Speed = {e.speed}')

e.start()
e.stop()
print(dir(e))
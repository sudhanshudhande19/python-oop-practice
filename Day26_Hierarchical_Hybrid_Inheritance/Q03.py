# Concept: Method reusability.

# Requirements:

    # Create Vehicle as the parent class.
    # Create Car, Bike, and Bus as child classes.
    # Vehicle should have a start() method.
    # Car should have a four_wheels() method.
    # Bike should have a two_wheels() method.
    # Bus should have a passenger_capacity() method.
    # Create one object of each class.
    # Call all available methods.

#_---------------------------------------------------------------------------------------------------


class Vehical:

    def start(self):

        print(f'Vehical Started')

class Car(Vehical):

    def four_wheels(self):
        print('Car has four wheels')

class Bike(Vehical):

    def tow_wheels(self):
        print('Bike has two wheels')

class Bus(Vehical):

    def passenger_capacity(self):
        print('Bus carries passengers')


c = Car()
b = Bike()
Bu = Bus()

c.start()
c.four_wheels()

b.start()
b.tow_wheels()

Bu.start()
Bu.passenger_capacity()
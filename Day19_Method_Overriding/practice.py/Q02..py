# Create a Vehicle class with a start() method. Override it in Car and Bike.

#---------------------------------------------------------------------------------------------


class Vehical:
    def start(self):
        print(f'Start The Company 1999')

class Car(Vehical):
    def start(self):
        print('1 Car Model is BMW')

class Bike(Car):
    def start(self):
        print('1 Bike Model is Holda')

a = Vehical()
b = Car()
e = Bike()

a.start()
b.start()
e.start()
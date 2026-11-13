# Concept: Hybrid Inheritance.

# Requirements:

    # Create Device as parent.
    # Computer and Mobile inherit from Device.
    # SmartDevice inherits from Computer and Mobile.
    # Device stores brand.
    # Computer stores RAM.
    # Mobile stores battery capacity.
    # SmartDevice should inherit from Computer and Mobile.
    # Display all inherited attributes.

#-------------------------------------------------------------------------------------------------

class device:

    def __init__(self,brand):
        self.brand = brand

class Computer(device):

    def __init__(self,brand,RAM):
        device.__init__(self,brand)
        self.RAM = RAM

class Mobile(device):

    def __init__(self,brand,battery_capacity):
        device.__init__(self,brand)
        self.battery_capacity = battery_capacity 

class SmartDevice(Computer,Mobile):

    def __init__(self,brand,RAM,battery_capacity):
        Computer.__init__(self,brand,RAM)
        Mobile.__init__(self,brand,battery_capacity)

    def info(self):
        print(f'Brand = {self.brand}')
        print(f'RAM = {self.RAM} GB')
        print(f'Battery = {self.battery_capacity} mAh')

s = SmartDevice('Samsung',8,5000)
s.info()

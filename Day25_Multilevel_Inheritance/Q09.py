# Concept: Method overriding.

# Requirements:

    # Create Device, Computer, and GamingComputer classes.
    # Device should contain a start() method.
    # Computer should override the start() method.
    # GamingComputer should override it again.
    # Create an object of GamingComputer.
    # Call the start() method.
    # Observe which method executes
#------------------------------------------------------------------------------------------------------------


class Device:

    def  start(self):
        pass

class Computer(Device):

    def start(self):
        super().start()
        pass

class gamingCompuetr(Computer):

    def start(self):
        super().start()
        print(f'Gaming Computer is starting')

s = gamingCompuetr()
s.start()
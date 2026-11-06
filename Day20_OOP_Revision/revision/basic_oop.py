"""
Day 20 - OOP Revision
basic_oop.py - Class, object, __init__, self, instance vs class variables
"""


class Car:
    wheels = 4                                   # class variable (shared by all cars)

    def __init__(self, brand, speed=0):
        self.brand = brand                       # instance variables (per object)
        self.speed = speed

    def accelerate(self, amount):                # instance method (uses self)
        self.speed += amount

    def show(self):
        print(f"{self.brand}: speed {self.speed} km/h, wheels {self.wheels}")


if __name__ == "__main__":
    print("--- Objects of a class ---")
    c1 = Car("Tata")
    c2 = Car("Honda", 20)
    c1.accelerate(40)
    c1.show()
    c2.show()

    print("\n--- Instance variable changes only ONE object ---")
    c2.accelerate(30)
    print("c1.speed:", c1.speed, "| c2.speed:", c2.speed)

    print("\n--- Class variable is shared ---")
    Car.wheels = 6
    print("c1.wheels:", c1.wheels, "| c2.wheels:", c2.wheels)

    print("\n--- Setting c1.wheels creates an INSTANCE variable ---")
    c1.wheels = 3
    print("c1.wheels:", c1.wheels, "| c2.wheels:", c2.wheels, "| Car.wheels:", Car.wheels)

    print("\n--- Inspecting with __dict__ and dir() ---")
    print("c1.__dict__ :", c1.__dict__)
    print("c2.__dict__ :", c2.__dict__)
    print("public names:", [n for n in dir(c1) if not n.startswith("__")])

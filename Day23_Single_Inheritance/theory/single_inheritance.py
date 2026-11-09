"""
Day 23 - Python OOP: Single Inheritance
theory/single_inheritance.py - Theory examples

Run this file and, for every line, say WHICH class's code is running.
"""


def heading(title):
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


# ---------------------------------------------------------
# 1. Basic single inheritance
# ---------------------------------------------------------
heading("1. Basic single inheritance")


class Parent:
    def show(self):
        print("This is Parent Class")


class Child(Parent):
    def display(self):
        print("This is Child Class")


obj = Child()
obj.show()          # inherited from Parent
obj.display()       # defined in Child


# ---------------------------------------------------------
# 2. Constructor: three cases
# ---------------------------------------------------------
heading("2. Constructors in inheritance")


class Person:
    def __init__(self, name):
        self.name = name


# Case A: the child has NO __init__ -> the parent's __init__ is used
class StudentA(Person):
    pass


a = StudentA("Rahul")
print("Case A:", a.name)


# Case B: the child has __init__ but forgets super() -> parent data is missing
class StudentB(Person):
    def __init__(self, name, marks):
        self.marks = marks


b = StudentB("Rahul", 85)
print("Case B: marks =", b.marks)
try:
    print(b.name)
except AttributeError as error:
    print("Case B: Error ->", error)


# Case C: the child calls super().__init__() -> everything is set
class StudentC(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks


c = StudentC("Rahul", 85)
print("Case C:", c.name, c.marks)


# ---------------------------------------------------------
# 3. Method overriding
# ---------------------------------------------------------
heading("3. Method overriding")


class Animal:
    def sound(self):
        print("Animal makes sound")

    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def sound(self):                 # replaces the parent's version
        print("Dog barks")


class Cat(Animal):
    def sound(self):                 # extends the parent's version
        super().sound()
        print("Cat meows")


d1 = Dog()
d1.sound()
d1.eat()                             # not overridden -> inherited

print("--- Cat (uses super) ---")
Cat().sound()


# ---------------------------------------------------------
# 4. Private attributes are NOT directly available in the child
# ---------------------------------------------------------
heading("4. Private (__x) vs protected (_x)")


class Account:
    def __init__(self, balance):
        self.__balance = balance         # private  -> stored as _Account__balance
        self._owner = "Rahul"            # protected (convention)

    def get_balance(self):
        return self.__balance


class SavingsAccount(Account):
    def show_owner(self):
        return self._owner               # OK: protected names are reachable

    def show_balance_directly(self):
        return self.__balance            # ERROR: becomes self._SavingsAccount__balance


acc = SavingsAccount(5000)
print("protected via child :", acc.show_owner())
print("private via parent method:", acc.get_balance())
try:
    acc.show_balance_directly()
except AttributeError as error:
    print("private via child   -> Error:", error)


# ---------------------------------------------------------
# 5. Checking relationships
# ---------------------------------------------------------
heading("5. isinstance, issubclass, __bases__, mro()")

print("isinstance(d1, Dog)      :", isinstance(d1, Dog))
print("isinstance(d1, Animal)   :", isinstance(d1, Animal))
print("isinstance(Animal(), Dog):", isinstance(Animal(), Dog))
print("issubclass(Dog, Animal)  :", issubclass(Dog, Animal))
print("Dog.__bases__            :", Dog.__bases__)
print("Dog.mro()                :", [cls.__name__ for cls in Dog.mro()])


# ---------------------------------------------------------
# 6. A complete example: Appliance -> WashingMachine
# ---------------------------------------------------------
heading("6. Appliance -> WashingMachine")


class Appliance:
    def __init__(self, brand, watts):
        if watts <= 0:
            raise ValueError("Power must be positive")
        self.brand = brand
        self.watts = watts

    def units_used(self, hours):                        # kWh
        return self.watts * hours / 1000

    def monthly_cost(self, hours_per_day, rate=8):
        return round(self.units_used(hours_per_day * 30) * rate, 2)

    def display(self):
        print(f"Brand: {self.brand} | Power: {self.watts} W")


class WashingMachine(Appliance):
    def __init__(self, brand, watts, capacity_kg):
        super().__init__(brand, watts)                  # parent validation is reused
        self.capacity_kg = capacity_kg

    def display(self):                                  # extend the parent's display
        super().display()
        print(f"Capacity: {self.capacity_kg} kg")

    def monthly_cost(self, hours_per_day, rate=8):      # parent's cost + water charge
        return super().monthly_cost(hours_per_day, rate) + 50


fan = Appliance("Usha", 75)
machine = WashingMachine("LG", 500, 7)

fan.display()
machine.display()
print("fan cost (8 h/day)    :", fan.monthly_cost(8))
print("machine cost (1 h/day):", machine.monthly_cost(1))
print("machine.units_used(2) :", machine.units_used(2), "(inherited)")

for item in [fan, machine]:
    print(type(item).__name__, "->", item.monthly_cost(2))

try:
    WashingMachine("X", -5, 7)
except ValueError as error:
    print("Child gets the parent's validation:", error)

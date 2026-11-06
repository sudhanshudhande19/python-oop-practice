"""
Day 20 - OOP Revision
inheritance.py - Single, multilevel, multiple, hierarchical inheritance, super(), MRO
"""


# --- Single inheritance ---
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} starts")


class Bike(Vehicle):
    pass


# --- Multilevel inheritance with super() at every level ---
class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language


# --- Multiple inheritance ---
class Father:
    def skill(self):
        print("Father: driving")


class Mother:
    def skill(self):
        print("Mother: cooking")

    def hobby(self):
        print("Mother: painting")


class Child(Father, Mother):
    pass


# --- Hierarchical inheritance ---
class Shape:
    def describe(self):
        print("I am a shape")


class Square(Shape):
    pass


class Triangle(Shape):
    pass


if __name__ == "__main__":
    print("--- Single ---")
    Bike("Yamaha").start()

    print("\n--- Multilevel ---")
    dev = Developer("Asha", 60000, "Python")
    print(dev.name, dev.salary, dev.language)
    print("MRO:", [c.__name__ for c in Developer.mro()])

    print("\n--- Multiple (left parent wins) ---")
    child = Child()
    child.skill()                                 # Father is first in the MRO
    child.hobby()                                 # only Mother has it
    print("MRO:", [c.__name__ for c in Child.mro()])

    print("\n--- Hierarchical ---")
    Square().describe()
    Triangle().describe()

    print("\n--- Checking relationships ---")
    print("issubclass(Developer, Person):", issubclass(Developer, Person))
    print("isinstance(dev, Employee)    :", isinstance(dev, Employee))
    print("Developer.__bases__          :", Developer.__bases__)

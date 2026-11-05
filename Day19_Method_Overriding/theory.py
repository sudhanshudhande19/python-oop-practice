"""
Day 19 - Python OOP: Method Overriding
theory.py - Examples from the theory section

Run this file and, for every line, say WHICH class's method is running.
"""


def heading(title):
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


# ---------------------------------------------------------
# 1. Basic method overriding
# ---------------------------------------------------------
heading("1. Basic method overriding")


class Animal:
    def sound(self):
        print("Animal makes a sound")

    def eat(self):
        print("Animal eats")


class Dog(Animal):
    def sound(self):                 # same name -> overrides Animal.sound
        print("Dog barks")


Animal().sound()                     # parent object -> parent version
Dog().sound()                        # child object  -> child version


# ---------------------------------------------------------
# 2. Not overridden -> inherited
# ---------------------------------------------------------
heading("2. Method that is NOT overridden")

d = Dog()
d.sound()                            # overridden
d.eat()                              # inherited from Animal


# ---------------------------------------------------------
# 3. Which method runs? (the MRO)
# ---------------------------------------------------------
heading("3. Search order (MRO)")

print([cls.__name__ for cls in Dog.mro()])


# ---------------------------------------------------------
# 4. Overriding with super()
# ---------------------------------------------------------
heading("4. Overriding with super()")


class Parent:
    def show(self):
        print("Parent method")


class Child(Parent):
    def show(self):
        super().show()               # reuse the parent's version
        print("Child method")


Child().show()


# ---------------------------------------------------------
# 5. Runtime polymorphism
# ---------------------------------------------------------
heading("5. Runtime polymorphism")


class Pet:
    def sound(self):
        print("Animal sound")


class Puppy(Pet):
    def sound(self):
        print("Bark")


class Kitten(Pet):
    def sound(self):
        print("Meow")


for pet in [Puppy(), Kitten(), Pet()]:
    pet.sound()                      # same call, different behaviour


# ---------------------------------------------------------
# 6. Overriding __init__ and __str__
# ---------------------------------------------------------
heading("6. Overriding __init__ and __str__")


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, marks {self.marks}"


print(Person("Amit"))
print(Student("Rahul", 85))


# ---------------------------------------------------------
# 7. Overloading is NOT supported: the last method wins
# ---------------------------------------------------------
heading("7. Same method name twice in ONE class")


class Demo:
    def show(self):
        print("no arguments")

    def show(self, x):               # replaces the first show()
        print("one argument:", x)


Demo().show(5)
try:
    Demo().show()
except TypeError as error:
    print("Error:", error)


# ---------------------------------------------------------
# 8. Simulating overloading
# ---------------------------------------------------------
heading("8. Simulating overloading (default args and *args)")


class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

    def total(self, *args):
        return sum(args)


calc = Calculator()
print("add(2, 3)        :", calc.add(2, 3))
print("add(2, 3, 4)     :", calc.add(2, 3, 4))
print("total(1, 2, 3, 4):", calc.total(1, 2, 3, 4))


# ---------------------------------------------------------
# 9. A parent method that calls self.method()
# ---------------------------------------------------------
heading("9. Parent method calling self.body()")


class Report:
    def print_report(self):
        print("--- REPORT ---")
        self.body()                  # runs the CHILD's body() for a child object

    def body(self):
        print("Default body")


class SalesReport(Report):
    def body(self):
        print("Sales: 50 items sold")


Report().print_report()
SalesReport().print_report()

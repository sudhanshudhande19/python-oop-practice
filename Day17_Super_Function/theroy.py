"""
Day 17 - Python OOP: super() Function
theory.py - Examples of super() and MRO

Run this file and read the output carefully.
Try to predict the output of each example BEFORE you run it.
"""


def heading(title):
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


# ---------------------------------------------------------
# 1. super() with constructor
# ---------------------------------------------------------
heading("1. super() with constructor")


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, marks):
        super().__init__(name)   # parent sets name
        self.marks = marks       # child sets marks


s1 = Student("Rahul", 85)
print(s1.name)
print(s1.marks)


# ---------------------------------------------------------
# 2. The problem: forgetting super() in the child constructor
# ---------------------------------------------------------
heading("2. What happens WITHOUT super() in the constructor")


class Person2:
    def __init__(self, name):
        self.name = name


class Student2(Person2):
    def __init__(self, name, marks):
        self.marks = marks       # parent constructor is never called


s2 = Student2("Rahul", 85)
print("marks:", s2.marks)
try:
    print("name:", s2.name)
except AttributeError as error:
    print("Error:", error)


# ---------------------------------------------------------
# 3. super() with methods (extend the parent's behaviour)
# ---------------------------------------------------------
heading("3. super() with methods (extend)")


class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        super().sound()          # run the parent method first
        print("Dog barks")       # then add the child's own behaviour


d1 = Dog()
d1.sound()


# ---------------------------------------------------------
# 4. Overriding WITHOUT super() (replace the parent's behaviour)
# ---------------------------------------------------------
heading("4. Overriding without super() (replace)")


class Cat(Animal):
    def sound(self):
        print("Cat meows")       # parent version is completely replaced


Cat().sound()


# ---------------------------------------------------------
# 5. Reusing the value returned by the parent method
# ---------------------------------------------------------
heading("5. Reusing the parent's returned value")


class Ticket:
    def price(self):
        return 300


class VIPTicket(Ticket):
    def price(self):
        return super().price() + 200   # parent's result + extra


print("VIP ticket price:", VIPTicket().price())


# ---------------------------------------------------------
# 6. super() in multilevel inheritance
# ---------------------------------------------------------
heading("6. super() in multilevel inheritance")


class Grandparent:
    def show(self):
        print("Grandparent class")


class Parent(Grandparent):
    def show(self):
        super().show()
        print("Parent class")


class Child(Parent):
    def show(self):
        super().show()
        print("Child class")


obj = Child()
obj.show()


# ---------------------------------------------------------
# 7. super() vs calling the parent class directly
# ---------------------------------------------------------
heading("7. super() vs direct parent call")


class Base:
    def __init__(self, name):
        self.name = name


class WithSuper(Base):
    def __init__(self, name, marks):
        super().__init__(name)           # no class name, no self
        self.marks = marks


class WithDirectCall(Base):
    def __init__(self, name, marks):
        Base.__init__(self, name)        # class name hard-coded, self required
        self.marks = marks


a = WithSuper("Rahul", 85)
b = WithDirectCall("Amit", 90)
print("super():      ", a.name, a.marks)
print("direct call:  ", b.name, b.marks)


# ---------------------------------------------------------
# 8. What is MRO?
# ---------------------------------------------------------
heading("8. MRO (Method Resolution Order)")

print("Child.mro():")
print(Child.mro())

print("\nReadable names:")
print([cls.__name__ for cls in Child.mro()])

print("\nChild.__mro__ (same thing, but a tuple):")
print(Child.__mro__)


# ---------------------------------------------------------
# 9. MRO in multiple inheritance (diamond shape)
# ---------------------------------------------------------
heading("9. Multiple inheritance (diamond) - Vehicle example")


class Vehicle:
    def start(self):
        print("Vehicle: start")


class Electric(Vehicle):
    def start(self):
        super().start()
        print("Electric: motor on")


class Petrol(Vehicle):
    def start(self):
        super().start()
        print("Petrol: engine on")


class Hybrid(Electric, Petrol):
    def start(self):
        super().start()
        print("Hybrid: ready")


Hybrid().start()
print("MRO:", [cls.__name__ for cls in Hybrid.mro()])
print("Notice: Electric's super() went to Petrol, not to Vehicle!")


# ---------------------------------------------------------
# 10. Useful extras
# ---------------------------------------------------------
heading("10. Useful extras")

print("Child.__bases__ :", Child.__bases__)
print("issubclass(Child, Grandparent):", issubclass(Child, Grandparent))
print("isinstance(obj, Parent)       :", isinstance(obj, Parent))
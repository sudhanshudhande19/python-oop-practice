# Concept: Multilevel Inheritance with methods.

# Requirements:
    # Create Animal, Mammal, and Dog classes.
    # Animal should have an eat() method.
    # Mammal should have a walk() method.
    # Dog should have a bark() method.
    # Create a Dog object.
    # Call all three methods.

#----------------------------------------------------------------------------------------------------------------


class Animal:

    def eat(self):
        print(f'Animal is eating')

class Mammal(Animal):

    def walk(self):
        print(f'Mammal is walking')

class Dog(Mammal):

    def brak(self):
        print('Dog  is Barking')

s = Dog()
s.eat()
s.walk()
s.brak()
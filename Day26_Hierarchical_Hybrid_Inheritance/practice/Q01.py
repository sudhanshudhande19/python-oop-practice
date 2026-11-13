# Concept: Basic Hierarchical Inheritance.

# Requirements:
    # Create one parent class Animal.
    # Create three child classes: Dog, Cat, and Cow.
    # Add an eat() method in Animal.
    # Add a bark() method in Dog.
    # Add a meow() method in Cat.
    # Add a sound() method in Cow.
    # Create separate objects for all three child classes.
    # Call the inherited and individual methods.

#-------------------------------------------------------------------------------------------------------


class Animal:

    def eat(self):
        print('Animal is eating')

class Dog(Animal):

    def bark(self):
        print('Dog is barking')

class Cat(Animal):

    def meow(self):
        print('Cat is Meowing')

class Cow(Animal):

    def sound(self):
        print(f'Cow is Mooing')

D = Dog()
C =Cat()
Co = Cow()

D.eat()
D.bark()

C.eat()
C.meow()

Co.eat()
Co.sound()
# Create an Animal parent class and a Dog child class.

# Concept: Inheriting Parent Methods.

# Requirements:

    # Create an Animal class.
    # Add a method eat().
    # Create a Dog class that inherits Animal.
    # Add a method bark().
    # Call both methods using a Dog object.

#-----------------------------------------------------------------------------------------------------


class Animal:

    def eat(self):
        print(f'Animal Eat a Food')

class Dog(Animal):

    def bark(self):
        print(f'Dog Sound = Bark')

s = Dog()
s.eat()
s.bark()
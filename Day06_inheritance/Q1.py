# Create a parent class Animal with a method:

# eat()

# Create a child class Dog that inherits from Animal.
# Add a method bark() to Dog.
# Create a Dog object and call both methods.
#---------------------------------------------------------------------------
class animal:
    def eat(self):
        print('Animal is Eating')

class dog(animal):
    def brak(self):
        print('Dog is Borking')

e1 = dog()

e1.eat()
e1.brak()
        
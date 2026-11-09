# reate an Animal parent class and a Cat child class.

# Concept: Method Overriding.

# Requirements:

    # Parent has a sound() method.
    # Child overrides the sound() method.
    # Display a different sound for Cat.
    # Use super() to call the parent method as well.

#----------------------------------------------------------------------------------------------------

class Animal:

    def sound(self):
        print(f'Animal Sound')

class Car(Animal):

    def sound(self):
        super().sound()
        print(f'Cat = Meow')

s = Car()
s.sound()
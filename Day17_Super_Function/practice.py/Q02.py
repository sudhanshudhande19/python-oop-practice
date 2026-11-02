# Create an Animal class with a sound() method.

# Create a Dog class that overrides sound().

# Requirements:

    # Call the parent method using super().
    # Print the dog's own sound.

#---------------------------------------------------------------------------------------------


class Animal:
    def sound(self):
        print('Animal Sound')

class Dog(Animal):

    def sound(self):
        super().sound()
        print('Dog = Barks')
        
        

e = Dog()
e.sound()
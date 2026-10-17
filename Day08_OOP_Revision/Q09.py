# Create a parent class Animal with a method sound().
# Create child classes:

    # Dog
    # Cat
    # Cow

# Override sound() in each child class.
# Create one object of each class and call the method.

#---------------------------------------------------------------------------------------

class Animal:
    def sound(self):
        print('Animal Sound ')

class dog(Animal):
    def  sound(self):
        print('Dog = Bark ')

class cat(Animal): 
    def sound(self):
        print('Cat  = Meow ')

class cow(Animal):
    def sound(self):
        print('Cow = Moo ')

e = Animal()
e.sound()

e = dog()
e.sound()

e = cat()
e.sound()

e = cow()
e.sound()
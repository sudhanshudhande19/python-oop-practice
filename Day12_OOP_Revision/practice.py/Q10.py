# Create a parent class Animal with a method sound().

# Create child classes:

    # Dog
    # Cat
    # Cow

# Requirements:

    # Override sound() in each child class.
    # Create objects of all three child classes.
    # Call the method for each object.

#----------------------------------------------------------------------------------------------

class Animal:
    def sound(self):
        print('Animal Sound')

class Dog(Animal):
    def sound(self):
        print('Dog = bark')

class cat(Animal):
    def sound(self):
        print('Cat = meow')

class cow(Animal):
    def sound(self):
        print('cow = moo')
s = Animal()
s1 = Dog()
s2 = cat()
s3 = cow()

s.sound()
s1.sound()
s2.sound()
s3.sound()
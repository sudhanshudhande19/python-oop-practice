# Create an Animal class with a sound() method. Create a Dog class that overrides it.

#---------------------------------------------------------------------------------------------------------------------


class Animal:
    def sound(self):
        print(f'Animal Sound')

class Dog(Animal):
    def sound(self):
        print(f'Dog = Barking')

c = Animal()
c.sound()
k =Dog()
k.sound()
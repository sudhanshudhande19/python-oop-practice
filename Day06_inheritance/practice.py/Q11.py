# Create a parent class Animal with a method sound() that prints "Animal makes a sound".

# Create child classes:

    # Dog
    # Cat
    # Cow

# Override the sound() method in each child class.
# Create one object of each class and call sound().

#------------------------------------------------------------------------------------------------------------------

class animal:

   def sound(self):
      print('Animal Makes a Sound')

class dog(animal):
   def sound(self):
      print('Dog Sound = Dog Barks')
      
class car(animal):
   def sound(self):
      print('Cat Sound = Cat Meows')

class cow(animal):
   def sound(self):
      print('Cow Sound = Cow Moos')
   

e = animal()
e.sound()

e1 = dog()
e1.sound()

e2 = car()
e2.sound()

e3 = cow()
e3.sound()


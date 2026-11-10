# Create a Camera class and a Phone class. Inherit both into a Smartphone class.

# Concept: Reusing Methods from Multiple Parents.

# Requirements:

    # Camera should have a take_photo() method.
    # Phone should have a make_call() method.
    # Smartphone should inherit both.
    # Smartphone should have an install_app() method.
    # Call all methods using a Smartphone object.

#--------------------------------------------------------------------------------------------------------------------------

class Camer:

    def take_photo(self):
        print('Photo Captured')

class Phone:

    def calling(self):
        print(f'Calling....')
class Smartphone(Camer,Phone):

    def app_installation(self):
        print('App Installed')

s = Smartphone()
s.take_photo()
s.calling()
s.app_installation()
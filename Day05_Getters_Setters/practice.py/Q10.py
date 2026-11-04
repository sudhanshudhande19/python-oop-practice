# Create a Circle class with _radius.
# Rules:

    # Radius must be greater than zero.
    # Use a getter and setter for the radius.
    # Create an area property that calculates the circle's area.
#------------------------------------------------------------
class circle:
    def __init__(self,radius):
        self.radius =radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,new_radius):
        if new_radius > 0:
            self._radius = new_radius
            print('Area =',3.14 * new_radius * new_radius)
        else:
            print('Enter The Valid Radius')

r_e = float(input('Enter The Radius ='))
obj = circle(r_e)
 
        
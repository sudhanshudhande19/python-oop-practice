# Create a Vector class and overload +.

# Requirements:

    # Store x and y coordinates.
    # Define __add__().
    # Add the x coordinates separately.
    # Add the y coordinates separately.
    # Return a new Vector object.
    # Display the resulting vector.

#------------------------------------------------------------------------------


class Vector:

    def __init__(self,x,y):
        self.x = x 
        self.y = y 

    def __add__(self, other):
        return self.x + other.x , self.y + other.y

s1 = Vector(5,2)
s2 = Vector(8,6)

sum = s1 + s2

print(sum)
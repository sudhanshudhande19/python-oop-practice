# Create a Vector class.

# Requirements:

    # Store x and y.
    # Implement __add__().
    # Add two vectors.
    # Return a new Vector object.

# Example:

    # Vector(2, 3) + Vector(4, 5)
    # Result: Vector(6, 8)
#------------------------------------------------------------------------------------------


class Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f'Vector ({self.x} , {self.y})'

e = Vector(2,3)
f = Vector(4,5)

total = e+f
print(total)
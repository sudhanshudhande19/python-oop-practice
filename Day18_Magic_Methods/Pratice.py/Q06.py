# Create a Number class.

# Requirements:

    # Store one numeric value.
    # Implement __add__().
    # Add two objects using +.
    # Return a new Number object.

#---------------------------------------------------------------------------------------


class Number:

    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


n1 = Number(10)
n2 = Number(20)

total = n1 + n2

print(total.value)
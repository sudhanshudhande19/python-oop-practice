# reate a Number class with __sub__().

# Subtract two objects using the - operator.

#--------------------------------------------------------------------------------------


class Number:

    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return Number(self.value - other.value)


n1 = Number(20)
n2 = Number(20)

total = n1 + n2

print(total.value)
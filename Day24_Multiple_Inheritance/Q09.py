# Create two parent classes with the same method name and inherit both into a child class.

# Concept: Method Resolution Order.

# Requirements:

    # Parent class A should contain a show() method.
    # Parent class B should also contain a show() method.
    # Child class should inherit A first and B second.
    # Call show() using a child object.
    # Check the MRO.

#----------------------------------------------------------------------------------------------------------------------------------

class A:
    def show(self):
        print("Method from Class A")


class B:
    def show(self):
        print("Method from Class B")


class Child(A, B):
    pass


obj = Child()

obj.show()

# Check MRO
print(Child.mro())
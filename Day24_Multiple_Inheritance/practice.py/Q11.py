# Create a diamond-shaped inheritance structure.

# Concept: Diamond Problem and MRO.

# Requirements:

    # Class A should have a show() method.
    # Class B should inherit A.
    # Class C should inherit A.
    # Class D should inherit B and C.
    # Use super() in each show() method.
    # Observe the method execution order.

#-----------------------------------------------------------------------------------------------------


class A:
    def show(self):
        pass

class B(A):

    def show(self):
        super().show()
        pass
class C(A):

    def show(self):
        super().show()
        pass

class D(B,C):

    def show(self):
        super().show()
        pass


x = D()
x.show()
print(D.mro())
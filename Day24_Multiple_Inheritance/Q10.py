# Create a four-class inheritance structure and examine its MRO.

# Concept: Understanding MRO.

# Requirements:

    # Create class A.
    # Create class B inheriting A.
    # Create class C inheriting A.
    # Create class D inheriting B and C.
    # Display MRO using both supported approaches.

#--------------------------------------------------------------------------------------------------------

class A:

    def show(self):
        print('A')

class B(A):

    def show(self):
        super().show()
        print('B')
class C(A):

    def show(self):
        super().show()
        print('C')
class D(B,C):
    def show(self):
        super().show()
        print('D')

x = D()

print(D.mro())
print(D.__mro__)
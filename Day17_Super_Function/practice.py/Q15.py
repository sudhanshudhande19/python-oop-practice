# Create a multiple inheritance example.

    # Classes:
    # A
    # B(A)
    # C(A)
    # D(B, C)

# Requirements:

    # Each class should have a show() method.
    # Use super() in each method
    # Create an object of D.
    # Call show().
    # Display D.mro().
    # Understand the method calling order.

#-----------------------------------------------------------------------------------------

class A:
    def show(self):
        print(f'A')
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

e = D()

print("Method Calls:")
e.show()

print("\nMRO:")
print(D.mro())
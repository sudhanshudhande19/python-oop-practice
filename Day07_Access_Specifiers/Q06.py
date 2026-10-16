# Create a Student class with a protected attribute _marks.
    # Create a method display_marks().

# Display the marks using the method, then access _marks directly outside the class and observe what happens.
# Goal: Understand that a single underscore is a convention, not strict access protection.

#------------------------------------------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self,marks):
        self._marks = marks

    def display_marks(self):
        print('Marks =',self._marks)


# Create object
s1 = Student(85)

# Access using method
s1.display_marks()

# Access directly outside the class
print("Direct Access =", s1._marks)
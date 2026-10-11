# Create a Student class with _marks.
# Rules:

    # Marks must be between 0 and 100.
    # Reject marks outside this range.
    # Display the marks using a getter.

# Test at least three different values.
#-----------------------------------------------------------------------


class Student:
    def __init__(self, marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Invalid Marks! Enter marks between 0 and 100.")


s1 = Student(85)
print("Marks:", s1.marks)

s1.marks = 95
print("Updated Marks:", s1.marks)

s1.marks = 120
print("Current Marks:", s1.marks)

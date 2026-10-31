# Create a Student object.

# Requirements:

    # Display its __dict__.
    # Update the marks.
    # Add a new attribute called grade.
    # Display __dict__ again.


# -----------------------------------------------------------------------------------------------------------------

class Student:

    def __init__(self, marks):
        self.marks = marks


e = Student(90)

# Display __dict__
print("Before changes:")
print(e.__dict__)

# Update marks
e.marks = 50

# Add new attribute
e.grade = "C"

# Display __dict__ again
print("\nAfter changes:")
print(e.__dict__)
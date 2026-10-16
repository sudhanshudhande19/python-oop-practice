# Create a Student class with a private attribute __marks.

# Requirements:
    # Create a method get_marks() to return the marks.
    # Create a method set_marks(marks) to update marks.
    # Accept only marks between 0 and 100.
    # Test valid and invalid values.
#------------------------------------------------------------------------------------------------



class Student:
    def __init__(self, marks):
        self.__marks = 0
        self.set_marks(marks)

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print(marks, "Valid Marks")
        else:
            print("Invalid Marks")


obj = Student(96)

print("Current Marks:", obj.get_marks())

obj.set_marks(85)
print("Updated Marks:", obj.get_marks())

obj.set_marks(105)
print("Current Marks:", obj.get_marks())

obj.set_marks(0)
print("Current Marks:", obj.get_marks())

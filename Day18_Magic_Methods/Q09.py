# Create a Student class.

# Requirements:

    # Store name and marks.
    # Implement __eq__().
    # Compare two students using ==.
    # Define equality based on marks.

#-----------------------------------------------------------------------------------------



class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks =marks

    def __eq__(self, value):
        return Student(self.marks + value.marks)

e = Student('Sudhanshu Dhande',66)

total  = e == e

print(total.marks)
# Create a Student class and overload ==.

# Requirements:

    # Store student name and marks.
    # Define __eq__().
    # Compare two students using their marks.
    # Return True if marks are equal.
    # Return False otherwise.

#---------------------------------------------------------------------------


class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks

    def __eq__(self, value):
        return self.marks == value.marks


s1 = Student('Sudhandhu Dhande',99)
s2 = Student('Kedar Hemane',49)


print(f'Name = {s1.name}')
print(f'Marks = {s1.marks}')
print(f'Name = {s2.name}')
print(f'Marks = {s2.marks}')

print(f'Tow Student marks is Same  ={s1.marks == s2.marks}')
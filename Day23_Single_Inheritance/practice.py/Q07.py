# Create a College parent class and a Student child class.

# Concept: Inheritance with Class and Instance Attributes.

# Requirements:

    # Parent stores college name.
    # Parent has a method to display college information.
    # Child stores student name and roll number.
    # Child displays both college and student information.

#------------------------------------------------------------------------------------------------------------


class College:

    def __init__(self,college):
        self.college = college

    def display(self):
        print(f'Colllege Name = {self.college}')

class Student(College):
    def __init__(self, college,name,roll_no):
        super().__init__(college)
        self.name = name
        self.roll_no = roll_no

    def display(self):
        super().display()
        print(f'Student Name = {self.name}')
        print(f'Roll No = {self.roll_no}')

s1 = Student('Karenjekar College of Engineering And Management','sudhanshu Dhande',101)
s1.display()
# Create a Student class with name, roll number, and marks. Display all details.

#------------------------------------------------------------------------------------------------


class Student:

    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number 
        self.marks = marks


s = Student('Sudhandhu Dhande',101,90)
print(f'Name = {s.name}')
print(f'Roll No = {s.roll_number}')
print(f'Marks = {s.marks}')
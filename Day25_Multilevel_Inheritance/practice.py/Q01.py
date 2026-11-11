# Concept: Basic Multilevel Inheritance.

# Requirements:
    # Create a Person class.
    # Create a Student class inheriting from Person.
    # Create a CollegeStudent class inheriting from Student.

# Steps to Solve:
    # Store name and age in Person.
    # Store roll number and marks in Student.
    # Store college name in CollegeStudent.
    # Create an object of CollegeStudent.
    # Display all information using methods.
#----------------------------------------------------------------------------------------------------


class Person:

    def __init__(self,name,age):
        self.name = name 
        self.age = age 

class Student(Person):
    def __init__(self, name, age,roll_no,marks):
        super().__init__(name, age)
        self.roll_no  = roll_no
        self.marks = marks

class CollegeStudent(Student):
    def __init__(self, name, age, roll_no, marks,college_name):
        super().__init__(name, age, roll_no, marks)
        self.college_name = college_name

    def display(self):
        print(f'Name         = {self.name}')
        print(f'Age          = {self.age}')
        print(f'Roll No      = {self.roll_no}')
        print(f'Marks        = {self.marks}')
        print(f'College Name = {self.college_name}')

s = CollegeStudent('Sudhanshu Dhande',22,101,95,'KCEM')
s.display()
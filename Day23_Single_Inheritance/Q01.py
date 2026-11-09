# Create a Person class and inherit it into a Student class.

# Concept: Basic Single Inheritance.

# Requirements:

    # Create a parent class named Person.
    # Store name and age.
    # Create a child class named Student.
    # Store roll_number and marks.
    # Create a method to display all student details.

#----------------------------------------------------------------------------------------------


class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age


class Student(Person):
    def __init__(self, name, age,roll_no,marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')
        print(f'Roll No = {self.roll_no}')
        print(f'Marks = {self.marks}')


s1 = Student('sudhanshu Dhade',22,101,85)
s1.display()
# Concept: Hybrid Inheritance with constructors.

# Requirements:

    # Create Person as the common parent.
    # Student and Employee inherit from Person.
    # Intern inherits from Student and Employee.
    # Person initializes name and age.
    # Student initializes roll number.
    # Employee initializes employee ID.
    # Intern initializes internship duration.
    # Use super() and understand MRO.
    # Print the complete intern profile.

#_-----------------------------------------------------------------------------------


class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):

    def __init__(self, name, age,roll_no):
        Person.__init__(self,name, age)
        self.roll_no = roll_no

class Employee(Person):

    def __init__(self, name, age,Employee_id):
        Person.__init__(self,name, age)
        self.Employee_id = Employee_id

class intern(Student,Employee):

    def __init__(self, name, age, roll_no,Employee_id,intership):
       Student.__init__(self,name, age, roll_no)
       Employee.__init__(self,name,age,Employee_id)
       self.intership = intership

    def info(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')
        print(f'Roll No = {self.roll_no}')
        print(f'Employee = {self.Employee_id}')
        print(f'Intership Duration = {self.intership} Months')

s = intern('Rahul',21,101,501,3)
s.info()

print(intern.mro())
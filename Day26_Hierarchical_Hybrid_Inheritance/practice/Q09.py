# Concept: Hybrid Inheritance.

# Requirements:

    # Create Person as parent class.
    # Student and Employee inherit from Person.
    # WorkingStudent inherits from Student and Employee.
    # Person stores name and age.
    # Student stores roll number.
    # Employee stores company name.
    # WorkingStudent should access the information from all classes.
    # Use super() where appropriate.
    # Display all information.

#-----------------------------------------------------------------------------------------------------------------------------------


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_number):
        Person.__init__(self, name, age)
        self.roll_number = roll_number


class Employee(Person):
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.company = company


class WorkingStudent(Student, Employee):
    def __init__(self, name, age, roll_number, company):
        Student.__init__(self, name, age, roll_number)
        Employee.__init__(self, name, age, company)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_number)
        print("Company:", self.company)


ws = WorkingStudent("Rahul", 22, 101, "ABC Company")
ws.display()
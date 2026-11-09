# Create an Employee parent class and a Developer child class.

# Concept: Inheritance with Instance Methods.

# Requirements:

    # Parent stores employee name and salary.
    # Parent has a method display_employee().
    # Child stores programming language.
    # Child has a method display_developer().
    # Display both parent and child information.

#-------------------------------------------------------------------------------------


class Employee:

    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary 

    def display_employee(self):
        print(f'Name = {self.name}')
        print(f'Salary = {self.salary}')

class Developer(Employee):
    def __init__(self, name, salary,pro_language):
        super().__init__(name, salary)
        self.pro_language = pro_language

    def display_employee(self):
        super().display_employee()
        print(f'Programming Language = {self.pro_language}')

emp = Developer('Sudhanshu Dhande',55000,'Python')
emp.display_employee()
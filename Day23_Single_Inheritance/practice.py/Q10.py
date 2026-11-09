# Create an Employee parent class and a Manager child class.

# Concept: Inheritance and Method Overriding.

# Requirements:

    # Parent stores employee name and basic salary.
    # Parent has a calculate_salary() method.
    # Child stores bonus.
    # Child overrides calculate_salary().
    # Calculate total salary including bonus.

#-----------------------------------------------------------------------------------------------


class Employee:

    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    def calculate_salary(self):
        return self.salary 

class Manager(Employee):

    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        super().calculate_salary()
        print(f'Total Salary = {self.salary + self.bonus}')

    def display(self):
        print(f'Name = {self.name}')
        print(f'Salary = {self.salary}')

s = Manager('Sudhanshu',50000,10000)
s.display()
s.calculate_salary()
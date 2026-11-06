# Create an Employee class with name and salary. Calculate annual salary.

#--------------------------------------------------------------------------------------------

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

c = Employee('Sudhanshu Dhande',55000)
print(f'Name = {c.name}')
print(f'Salary = {c.salary}')
print(f'Annual Salary = {c.salary * 12}')
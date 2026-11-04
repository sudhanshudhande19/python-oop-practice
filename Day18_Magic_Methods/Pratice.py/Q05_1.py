# Create an Employee class with:

    # name
    # salary

# Implement both __str__() and __repr__().

#-------------------------------------------------------------------------------------------------


class Employee:
    def __init__(self,name,salary):
        self.name =name
        self.salary = salary

    def __str__(self):
        return f'Name = {self.name}\nSalary = {self.salary}'

    def __repr__(self):
        return f'Name = {self.name} , Salary = {self.salary}'
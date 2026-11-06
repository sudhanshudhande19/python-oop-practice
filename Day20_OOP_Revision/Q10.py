# Create an Employee class with a from_string() class method that creates an employee from a string.

#------------------------------------------------------------------------------------------------------------------------------------------------


class Employee:

    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    @classmethod
    def from_string(cls,data):
        name,salary = data.split('-')
        return cls(name,int(salary))


s1 = Employee.from_string('Sudhanhsu-85000')
print(f'Name = {s1.name}')
print(f'Salary = {s1.salary}')    
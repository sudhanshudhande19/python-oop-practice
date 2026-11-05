print(f'===========Employee Management System===========')

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary =salary

    def calculate_salary(Self):
        return Self.salary

class Manager(Employee):
    def calculate_salary(Self):
        super().calculate_salary()
        bound = 10000 
        print(f'Manager Salary = {Self.salary + bound}')

class Developer(Employee):

    def calculate_salary(Self):
        super().calculate_salary()
        bound = 20000
        print(f'Developer Salary = {Self.salary + bound}')

class Intern(Employee):

    def calculate_salary(Self):
        super().calculate_salary()
        bonud = 15000
        print(f'Intern Salary = {Self.salary + bonud}')








m = Manager('Pranay',80000)
print(f'Name = {m.name}')
print(f'Salary = {m.salary}')
m.calculate_salary()

print('---------------------')

d = Developer('Sudhanshu',90000)
print(f'Name = {d.name}')
print(f'Salary = {d.salary}')
d.calculate_salary()

print('---------------------------')

i = Intern('Kedar',50000)
print(f'Name = {i.name}')
print(f'Salary = {i.salary}')
i.calculate_salary()

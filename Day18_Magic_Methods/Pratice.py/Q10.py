# Create an Employee class.

# Requirements:

    # Store name and salary.
    # Implement __lt__().
    # Compare employees using <.

#--------------------------------------------------------------------------


class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __It__(self,other):
        return self.salary < other.salary


e = Employee('Sudhanshu Dhande',80000)
print(f'Name = {e.name}')
print(f'Salary = {e.salary}')

f = Employee('Kunal',70000)
print(f'Name = {f.name}')
print(f'Salary = {f.salary}')

print(f'Salary = {f.salary < e.salary}')
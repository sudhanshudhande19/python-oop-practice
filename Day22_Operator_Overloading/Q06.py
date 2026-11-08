# Create an Employee class and overload >.

# Requirements:

    # Store employee name and salary.
    # Define __gt__().
    # Compare the salaries of two employees.
    # Return a Boolean result.
    # Identify the employee with the higher salary.

#--------------------------------------------------------------------------------------------------


class Employee:

    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee('Sudhanshu',55000)
emp2 = Employee('Kunal',40000)
s = [emp1,emp2]

for i in s:
    print(f'Name = {i.name}')
    print(f'Salary = {i.salary}')
    print('--------------------------')

print(emp1 > emp2)
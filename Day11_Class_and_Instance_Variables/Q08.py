# Create an Employee class with instance variables name and salary.

# Requirements:

    # Create three employees.
    # Update the salary of one employee.
    # Display all employees.
    # Ensure that updating one employee's salary does not change the others.

#-------------------------------------------------------------------------------------------------------------------------------------


class Employee :

    def __init__(self,name):
        self.name = name
        self.salary = 90000


s1 = Employee('Sudhanshu')
s1.salary = 1000000
print(f'{s1.name} : {s1.salary}')

s2 =Employee('Kunal')
print(f'{s2.name} : {s2.salary}')

s3 = Employee('Ayush')
print(f'{s3.name} : {s3.salary}')
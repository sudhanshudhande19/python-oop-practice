# Create an Employee class with:

    # Class variable employee_count = 0
    # Instance variables employee_id and name

# Requirements:

    # Automatically generate a unique ID for each employee.
    # Increase the employee count whenever an object is created.
    # Create five employees and display their IDs.

#-------------------------------------------------------------------------------------------------------------


class Employee:
    employee_count = 0

    def __init__(self,name):
        self.name = name
        Employee.employee_count += 1
        self.employee_id = Employee.employee_count


    def show(self):
        print(f'Name = {self.name}')
        print(f'Employee ID = {self.employee_id}')
        print('-------------------------')

e1 = Employee('Sudhanshu')
e2 = Employee('Kedar')
e3 = Employee('Kunal')
e4 = Employee('Aditya')
e5 = Employee('Aniket')

e1.show()
e2.show()
e3.show()
e4.show()
e5.show()
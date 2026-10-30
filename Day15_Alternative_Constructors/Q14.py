# Create an Employee class with:

    # Class variable employee_count = 0
    # Instance variables employee_id and name

# Requirements:

    # Automatically generate a unique ID for each employee.
    # Increase the employee count whenever an object is created.
    # Create five employees and display their IDs.

#-------------------------------------------------------------------------------------------------------------------------------

class Employee:
    employee_count = 0

    def __init__(self,employee_id,name):
        self.employee_id = employee_id
        self.name = name
        Employee.employee_count += 1
    
    def show(self):
        print(f'Employee Id = {self.employee_id}')
        print(f'Name = {self.name}')
        print('--------------------------------')
e1 = Employee(101,'Sudhanshu')
e2 = Employee(102,'kunal')
e3 = Employee(103,'kedar')
e4 = Employee(104,'aditya')
e5 = Employee(105,'ayush')

e1.show()
e2.show()
e3.show()
e4.show()
e5.show()

print(f'Total Employee = {e1.employee_count}')
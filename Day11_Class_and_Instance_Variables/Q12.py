# Create an Employee class with a class variable employee_count = 0.

# Requirements:

    # Increase the count whenever an employee is created.
    # Assign a unique employee ID to each object.
    # Create five employees.
    # Display their IDs and names.

# Hint: Use the class counter to generate the next ID.

#-------------------------------------------------------------------------------------------------------

class Employee:
    employee_count = 0

    def __init__(self,name):
        self.name = name
        Employee.employee_count += 1
        self.employee_id  = self.employee_count



e1 = Employee('Rahul')
e2 = Employee('Priya')
e3 = Employee('Amit')
e4 = Employee('Neha')
e5 = Employee('Rohan')

print(f'Employee ID: {e1.employee_id}, Name: {e1.name}')
print(f'Employee ID: {e2.employee_id}, Name: {e2.name}')
print(f'Employee ID: {e3.employee_id}, Name: {e3.name}')
print(f'Employee ID: {e4.employee_id}, Name: {e4.name}')
print(f'Employee ID: {e5.employee_id}, Name: {e5.name}')
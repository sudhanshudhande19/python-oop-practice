# Create an Employee class with:

    # Class variable: employee_count = 0
    # Instance variables: employee_id, name

# Requirements:

    # Generate a unique ID whenever an employee is created.
    # Create a class method get_employee_count().
    # Create five employees and display the count.
#---------------------------------------------------------------------------------------------

class Employee:

    employee_count = 0

    def __init__(self,name):
        self.name = name
        Employee.employee_count += 1
        self.employee_id = self.employee_count

    
    @classmethod
    def get_employee_count(self):
        for i in range (1,self.employee_count+1):
            print(f'Employee ID = {i}')
        
        print(f'Toal Employee = {self.employee_count}')
e1 = Employee('Sudhanshu')
e2 = Employee('Kunal')
e3 = Employee('Kedar')
e4 = Employee('Aditya')
e5 = Employee('Aniket')

Employee.get_employee_count()
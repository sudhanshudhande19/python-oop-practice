# Create an Employee class with:

    # employee_id
    # name
    # department
    # monthly_salary

# Methods:

    # display_details()
    # calculate_annual_salary()
# Create at least three employees.

#-------------------------------------------------------------------------------------------------

class Employee:

    def __init__(self,employee_id,name,deparment,monthly_salary):
        self.employee_id = employee_id
        self.name =name
        self.deparment = deparment
        self.monthly_salary = monthly_salary


    def display_details(self):
        print(f'Employee  ID = {self.employee_id}')
        print(f'Name = {self.name}')
        print(f'Deparment = {self.deparment}')
        print(f'Monthly Salary = {self.monthly_salary}')

    def calculate_annunal_salary(self):
        print(f'Annual Salary = {self.monthly_salary * 12}')
        print('--------------------------------------------')


e1 = Employee(101,'sudhanshu','Software Development',150000)
e2 = Employee(102,'Kedar','Cloud Services',80000)
e3 = Employee('103','Kunal','Cybersecurity ',55000)

e1.display_details()
e1.calculate_annunal_salary()

e2.display_details()
e2.calculate_annunal_salary()

e3.display_details()
e3.calculate_annunal_salary()
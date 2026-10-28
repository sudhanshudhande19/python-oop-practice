# Create an Employee class with:

    # Class variable: company_name = "Tech Solutions"
    # Instance variables: name, salary

# Requirements:

    # Create a class method display_company().
    # Display the company name without creating an object.
    # Test the method using the class name.

#------------------------------------------------------------------------------------------------------

class Employee:
    company_name = 'Tech Solutions'

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def display_company(cle):
        print(f'Company Name = {cle.company_name}')

    def show(self):
        print(f'Employee Name = {self.name}')
        print(f'Salary = {self.salary}')


Employee.display_company()

e1 = Employee('Sudhanshu Dhande',80000)
e1.show()
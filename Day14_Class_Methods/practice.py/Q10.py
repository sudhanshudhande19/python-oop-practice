# Create a Company class with:

    # Class variables: company_name, employee_count
    # Instance variable: employee_name

# Requirements:

    # Create a class method to update the company name.
    # Create a class method to display the employee count.
    # Create at least four employee objects.
    # Display the company information.

#-----------------------------------------------------------------------------------

class Company:
    company_name = ''
    employee_count = 0

    def __init__(self,employee_name):
        self.employee_name = employee_name
        Company.employee_count += 1

    @classmethod
    def Update_company_name(cls,new_company):
        cls.company_name = new_company
        print(f'Company Name = {cls.company_name}')

    @classmethod
    def display_employee_count(self):
        print(f'Total employee = {self.employee_count}')

e1 = Company('Sudhanshu')
e2 = Company('Kunal')
e3 = Company('Kedar')

Company.Update_company_name('Deloite')
print(f'employee Name = {e1.employee_name}')
print(f'employee Name = {e2.employee_name}')
print(f'employee Name = {e3.employee_name}')
e1.display_employee_count()
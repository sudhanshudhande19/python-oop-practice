# Create a Department class with:

    # Class variable: organization_name = "ABC Corporation"
    # Instance variables: department_name, employee_name
    # Create at least three objects for different departments.

# Requirements:

    # Display the organization and department details.
    # Update the organization name using the class name.
    # Override the organization name for one object only.
    # Explain the output.

#----------------------------------------------------------------------------------------------------------------


class Department:
    organization_name = 'ABC Corporation'

    def __init__(self,department_name, employee_name):
        self.department_name = department_name
        self.employee_name = employee_name


e1 = Department('Marketing','Sudhanshu')
e2 = Department('Product BI','Kunal')
e3 = Department('Product Testing','Amit')

print(f'organization = {Department.organization_name},Department = {e1.department_name}')
print(f'organization = {Department.organization_name},Department = {e2.department_name}')
print(f'organization = {Department.organization_name},Department = {e3.department_name}')
print('--------------------------------')
Department.organization_name = 'BMC Corporation'
print(f'organization = {Department.organization_name},Department = {e1.department_name}')
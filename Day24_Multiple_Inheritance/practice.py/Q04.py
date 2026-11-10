# Create an Employee class and a Department class. Inherit both into an EmployeeDetails class.

# Concept: Multiple Parent Attributes.

# Requirements:

    # Employee stores employee name and ID.
    # Department stores department name and department code.
    # EmployeeDetails stores salary.
    # Use all parent attributes in the child class.
    # Display complete details.

#-------------------------------------------------------------------------------------------------------------------------------------------------


class Employee:

    def __init__(self,name,id):
        self.name = name 
        self.id = id 

class Department:

    def __init__(self,department_name,department_code):
        self.department_name = department_name  
        self.department_code = department_code

class EmployeeDetails(Employee, Department):
    def __init__(self, name, id,salary):
        super().__init__(name, id)
        self.salary = salary

e = EmployeeDetails('Sudhanshu','A101',50000)
d = Department('Coding','c22')

print(f'Name = {e.name}')
print(f'ID = {e.id}')
print(f'Department = {d.deoartment_name}')
print(f'Department Code = {d.deoartment_code}')
print(f'Salary = {e.salary}')
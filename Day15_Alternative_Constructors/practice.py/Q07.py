# Create an Employee class with:

    # employee_id
    # name
    # department
    # monthly_salary

# Requirements:

    # Create a class method from_dict(data).
    # Read employee details from a dictionary.
    # Convert salary to a numeric value.
    # Calculate annual salary.
    # Display the employee details.
#----------------------------------------------------------------------------------------------------
class Employee:

    def __init__(self, employee_id, name, department, monthly_salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.monthly_salary = monthly_salary

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['employee_id'],
            data['name'],
            data['department'],
            float(data['monthly_salary'])
        )


e1 = Employee.from_dict({
    'employee_id': 101,
    'name': 'Sudhanshu',
    'department': 'IT',
    'monthly_salary': '25000'
})

print(f'Employee ID = {e1.employee_id}')
print(f'Employee Name = {e1.name}')
print(f'Employee Department = {e1.department}')
print(f'Monthly Salary = {e1.monthly_salary}')
print(f'Annual Salary = {e1.monthly_salary * 12}')
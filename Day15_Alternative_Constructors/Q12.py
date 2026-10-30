# Create an Employee class with:

    # name
    # department
    # monthly_salary

# Requirements:

    # Create from_string(data).
    # Accept input such as "Priya,AI,45000".
    # Reject negative salaries.
    # Calculate annual salary.
    # Calculate a 10% bonus on annual base salary.
    # Display the final compensation details.

#-----------------------------------------------------------------------------------------------------


class Employee:

    def __init__(self,name,department,monthly_salary):
        self.name = name
        self.department = department
        self.monthly_salary = monthly_salary

    @classmethod
    def from_string(cls,data):
        try:
            name,department,monthly_salary = data.split(',')

            monthly_salary = int(monthly_salary)
            if monthly_salary < 0:
                print('Reject The Negative Salary')
                return None

            return cls(name,department,monthly_salary)
        
        except ValueError:
            print("Invalid Numeric Input")
            return None

e1 = Employee.from_string('Rahul,101,85')

if e1:
    print(f'Name = {e1.name}')
    print(f'Department = {e1.department}')
    print(f'Monthly Salary = {e1.monthly_salary}')
    print(f'Annual Salary = {e1.monthly_salary * 12}')
    print(f'Annual Bonus  = {(e1.monthly_salary * 12)/ 10}')          
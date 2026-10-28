# Create an Employee class with:

    # name
    # monthly_salary

# Requirements:

    # Create a class method from_string(data).
    # Accept input in the format "Rahul,35000".
    # Convert the salary to a numeric value.
    # Create and return an employee object.
    # Display the employee's annual salary.

#------------------------------------------------------------------------------------

class employee:
    def __init__(self,name,monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    @classmethod
    def from_string(cls,data):
        name,monthly_salary = data.split(',')
        return cls(name.strip(),int(monthly_salary))

    def show(self):
        print(f'Employee Name = {self.name}')
        print(f'Monthly Salary = ₹{self.monthly_salary}')
        print(f'Annual Salary = {self.monthly_salary * 12}')
        print('-------------------------')


s1 = employee('Sudhanshu',85)
s1.show()


s2 = employee.from_string("Rahul,35000")
s2.show()


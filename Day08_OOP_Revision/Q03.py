# Create an Employee class with:
    # name
    # monthly_salary

# Requirements:
    # Create a method annual_salary().
    # Create a method display_details().
    # Create at least three employees and display their annual salaries.

# Formula: Annual salary = monthly salary × 12.

#-----------------------------------------------------------------------------------------------------

class employee:
    def __init__(self,name,monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return  self.monthly_salary * 12

    def display_details(self):
        print(f'Name = {self.name}')
        print(f'Monthly Salary = {self.monthly_salary}')
        print(f'Annual Salary = {self.annual_salary()}')
        print('--------------------------------------------------------')

e = employee('sudhanshu',55000)
e1 = employee('Rahul',45000)
e2 = employee('Prachi',35000)

e.annual_salary()
e.display_details()

e1.annual_salary()
e1.display_details()

e2.annual_salary()
e2.display_details()

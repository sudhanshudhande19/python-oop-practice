# Create an Employee class with:
# name
# department
# salary

# Create methods:
# display_details()
# annual_salary()

# Create two employees and display their annual salaries.
#--------------------------------------------------------------------

class employee:
    def __init__(self,name,deparment,salary):
        self.name = name
        self.deparment = deparment
        self.salary = salary

    def display_detail(self):
        print(f'Name= {self.name}\nDeparment = {self.deparment}\nSalary = {self.salary}\n')

    def annual_salary(self):
        print(f'Annual Salary = {self.salary   * 12}')
        print('---------------------------------------------------------')

obj = employee('Sudhanshu Dhande','AI',55000)
obj2 = employee('Pranay Dhande','CSE',72000)

obj.display_detail()
obj.annual_salary()

obj2.display_detail()
obj2.annual_salary()
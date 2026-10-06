# Create an Employee class with:

# 1.name
# 2.basic_salary

# Create methods:
# 1.annual_salary()
# 2.salary_after_bonus()

# Assume the bonus is 10% of the annual salary.
#-------------------------------------------------------------------------

class Employee:
    name = ''
    salary = 0

    def annual_salary(self):
        return self.salary * 12

    def salary_after_bouns(self):
        return self.annual_salary() * 1.10
    
    def info(self):
        print(f"Name = {self.name}")
        print(f"Annual Salary = {self.annual_salary()}")
        print(f"Salary After 10% Bonus = {self.salary_after_bouns()}")
        print()

obj = Employee()
obj2 = Employee()

obj.name = "Sudhanshu Dhande"
obj.salary = 80000

obj2.name = "Pranay Dhande"
obj2.salary = 100000

obj.info()
obj2.info()
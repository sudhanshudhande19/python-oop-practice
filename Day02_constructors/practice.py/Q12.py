# Create an Employee class with:
# 1.name
# 2.basic_salary

# Create methods:
# 1.monthly_salary()
# 2.annual_salary()
# 3.bonus()
# 4.final_annual_salary()

# Assume the bonus is 10% of the annual salary.
#---------------------------------------------------------------------
class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary
    
    def monthly_salary(self):
        return self.basic_salary
    
    def annual_salary(self):
        return self.monthly_salary() * 12

    def bonus(self):
        return self.annual_salary() * 0.10

    def final_annual_salary(self):
        return self.annual_salary() + self.bonus()

    def info(self):
        print(f"Employee Name : {self.name}")
        print(f"Monthly Salary : {self.monthly_salary()}")
        print(f"Annual Salary : {self.annual_salary()}")
        print(f"Bonus (10%) : {self.bonus()}")
        print(f"Final Annual Salary: {self.final_annual_salary()}")

emp1 = Employee("Sudhanshu", 50000)
emp1.info()
# Create a parent class Employee with:
    # name
    # basic_salary
    # annual_salary()

# Create two child classes:
    # Manager
    # Developer

# Requirements:

    # A manager receives a 20% annual bonus.
    # A developer receives a 10% annual bonus.
    # Use separate methods to calculate each employee's final annual salary.
# Assume the bonus is calculated from 12 months of basic salary.
#--------------------------------------------------------------------------------------------------


class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def annual_salary(self):
        return self.basic_salary * 12


class Manager(Employee):
    def bonus(self):
        return self.annual_salary() * 20 / 100

    def final_salary(self):
        return self.annual_salary() + self.bonus()


class Developer(Employee):
    def bonus(self):
        return self.annual_salary() * 10 / 100

    def final_salary(self):
        return self.annual_salary() + self.bonus()


e1 = Manager("Sudhanshu", 30000)
print("Manager Annual Salary:", e1.annual_salary())
print("Manager Bonus:", e1.bonus())
print("Manager Final Salary:", e1.final_salary())

print("-----------------------")

e2 = Developer("Kunal", 30000)
print("Developer Annual Salary:", e2.annual_salary())
print("Developer Bonus:", e2.bonus())
print("Developer Final Salary:", e2.final_salary())

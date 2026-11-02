# Create an Employee class with:

    # name
    # basic_salary
    # calculate_salary()

# Create a Manager class.

# Requirements:

    # Use super() in the constructor.
    # Override calculate_salary().
    # Call the parent method using super().
    # Add a 20% bonus to the parent's calculated salary.

#---------------------------------------------------------------------------------------------------


class Employee:
    def __init__(self,name,basic_salary):
        self.name =name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary

class Manager(Employee):
    def __init__(self, name, basic_salary):
        super().__init__(name, basic_salary)

    def calculate_salary(self):
        parent_salary = super().calculate_salary()
        bonus = parent_salary * 0.20
        return parent_salary + bonus


m = Manager("Sudhanshu Dhande", 50000)

print(f"Name = {m.name}")
print(f"Basic Salary = {m.basic_salary}")
print(f"Total Salary = {m.calculate_salary()}")
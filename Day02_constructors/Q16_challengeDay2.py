# Day 02 Challenge
# Employee Management
#-----------------------------------------------

class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def apply_bonus(self):
        if self.salary < 30000:
            return self.annual_salary() * 0.15
        elif self.salary <= 60000:
            return self.annual_salary() * 0.10
        else:
            return self.annual_salary() * 0.05

    def display_details(self):
        print(f"Name           : {self.name}")
        print(f"Employee ID    : {self.employee_id}")
        print(f"Department     : {self.department}")
        print(f"Monthly Salary : ₹{self.salary}")
        print(f"Annual Salary  : ₹{self.annual_salary()}")
        print(f"Bonus          : ₹{self.apply_bonus()}")
        print(f"Total Annual Pay : ₹{self.annual_salary() + self.apply_bonus()}")
        print("-" * 40)



emp1 = Employee("Sudhanshu", "EMP101", "IT", 25000)
emp2 = Employee("Rahul", "EMP102", "HR", 45000)
emp3 = Employee("Priya", "EMP103", "Finance", 80000)


emp1.display_details()
emp2.display_details()
emp3.display_details()
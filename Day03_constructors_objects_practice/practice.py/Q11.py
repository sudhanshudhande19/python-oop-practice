# Create an Employee class with:
# name
# salary
# performance_score

# Create methods:
# calculate_bonus()
# final_salary()
# display_details()

# Bonus rules:
# Score >= 90 → 20% bonus
# Score >= 75 → 15% bonus
# Score >= 60 → 10% bonus
# Score < 60  → No bonus

# Create at least 3 employees.
# ------------------------------------------------------------
class Employee:
    def __init__(self, name,salary,performance_score):
        self.name = name
        self.salary = salary
        self.performance_score = performance_score


    def calculate_bonus(self):
        if self.performance_score >= 90:
            return 20
        elif self.performance_score >= 75:
            return  15
        elif self.performance_score >= 60:
            return  10
        else:
            return 'NO Bouns'
    def final_salary(self):
        bonus =  (self.salary * self.calculate_bonus()) /100
        return self.salary + bonus
    def display_details(self):
        print(f"Name           : {self.name}")
        print(f'Salary         : {self.salary}')
        print(f'Performance Score : {self.performance_score}')
        print(f"Bonus          : ₹{self.calculate_bonus()}")
        print(f"Final Salary : ₹{self.final_salary()}")
        print("-" * 40)



emp1 = Employee("Sudhanshu",  25000,95)
emp2 = Employee("Rahul", 45000,63)
emp3 = Employee("Priya", 80000,76)


emp1.display_details()
emp2.display_details()
emp3.display_details()
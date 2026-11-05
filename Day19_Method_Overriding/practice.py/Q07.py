# Create an Employee class with a calculate_salary() method. Override it in Manager and add a bonus.

#---------------------------------------------------------------------------------------------------------------------

class Employee:

    def calculate_salary(Self):
        return 50000

class Manager(Employee):
    def calculate_salary(Self):
        base_salary = super().calculate_salary()
        bonus = 10000
        return base_salary + bonus

m = Manager()
print(f'Manager Salary = {m.calculate_salary()}')
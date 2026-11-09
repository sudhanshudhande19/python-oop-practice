print('=============================================================')
print('                 Employee Management System                  ')
print('=============================================================')

class Employee:

    def __init__(self,employee_name,employee_id,basic_salary):
        self.employee_name = employee_name 
        self.employee_id = employee_id 
        self.basic_salary = basic_salary 

    def display_employee(self):
        print(f'Employee Name = {self.employee_name}')
        print(f'Employee ID {self.employee_id}')
        print(f'Basic Salary = {self.basic_salary}')

class Manager(Employee):

    def __init__(self, employee_name, employee_id, basic_salary,department,bonus):
        super().__init__(employee_name, employee_id, basic_salary)
        self.department = department
        self.bonus = bonus

    def  calculate_total_salary(self):
        print(f'Total Monthly Salary = {self.basic_salary + self.bonus}')

    def display_manager(self):
        print(f'Department = {self.department}')
        print(f'Bonus = ₹{self.bonus}')

    def calculate_annual_Salary(self):
        annual = (self.basic_salary + self.bonus) * 12
        print(f'Annual Salary = ₹{annual}')

class Developer(Employee):
    def __init__(self, employee_name, employee_id, basic_salary,programming_lang,project_count):
        super().__init__(employee_name, employee_id, basic_salary)
        self.programming_lang = programming_lang
        self.project_count = project_count

    def display_developer(self):
        print(f'Programming Language = {self.programming_lang}')
        print(f'Project Count = {self.project_count}')

    def calculate_project_bonus(self):
        print(f'Project Bonus = {self.project_count * 1000}')

    def calculate_total_salary(self):
        total = self.basic_salary + (self.project_count * 1000)
        print(f'Total Salary = ₹{total}')
print('')
m = Manager('Rahul','E101',30000,'IT',10000,)
m.display_employee()
m.display_manager()
m.calculate_total_salary()
m.calculate_annual_Salary()
print()
print("===== DEVELOPER DETAILS =====")
print()
k = Developer('Amit','D101',25000,'Python',5,)
k.display_employee()
k.display_developer()
k.calculate_project_bonus()
k.calculate_total_salary()
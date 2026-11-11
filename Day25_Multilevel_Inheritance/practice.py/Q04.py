# Concept: Multilevel Inheritance with salary.

# Requirements:

    # Create Employee, Developer, and SeniorDeveloper classes.
    # Employee stores employee name and basic salary.
    # Developer stores programming language.
    # SeniorDeveloper stores experience.
    # Add a method to calculate annual salary.
    # Display complete employee information.

#-----------------------------------------------------------------------------------------


class Employee:

    def __init__(self,name,basic_salary):
        self.name = name
        self.basic_salary = basic_salary

class Developer(Employee):

    def __init__(self, name, basic_salary,programming_language):
        super().__init__(name, basic_salary)
        self.programming_language = programming_language

class SeniorDeveloper(Developer):

    def __init__(self, name, basic_salary, programming_language,Experience):
        super().__init__(name, basic_salary, programming_language)
        self.Experience = Experience

    def calculate_annual_salary(self):
        print(f'Annual Salary = {self.basic_salary * 12}')

s = SeniorDeveloper('Sudhanshu Dhande',25000,'Python',5)

print(f'Name = {s.name}')
print(f'Basic Salary = {s.basic_salary}')
print(f'Programming Language = {s.programming_language}')
print(f'Experienxce = {s.Experience}')
s.calculate_annual_salary()
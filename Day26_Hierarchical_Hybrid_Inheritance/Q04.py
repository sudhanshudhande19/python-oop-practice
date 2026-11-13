# Concept: Hierarchical Inheritance with salary details.

# Requirements:

    # Create Employee parent class.
    # Create three child classes.
    # Store employee name and basic salary in Employee.
    # Manager stores team size.
    # Developer stores programming language.
    # Designer stores design tool.
    # Display complete details for each employee.


#------------------------------------------------------------------------------------------------------------------------------

class Employee:

    def __init__(self,name,basic_salary):
        self.name = name 
        self.basic_salary = basic_salary

class Manager(Employee):

    def __init__(self, name, basic_salary,team_size):
        super().__init__(name, basic_salary) 
        self.team_size = team_size

class Developer(Employee):

    def __init__(self, name, basic_salary,programming_language):
        super().__init__(name, basic_salary)
        self.programming_language = programming_language

class Designer(Employee):

    def __init__(self, name, basic_salary,design_tool):
        super().__init__(name, basic_salary)
        self.design_tool = design_tool

m = Manager('Rahul',60000,10)
d = Developer('Amit',50000,'Python')
de = Designer('Priya',45000,'Figma')

print(f'Manager   = {m.name}, Salary = {m.basic_salary},  Team = {m.team_size}')
print(f'Developer = {d.name}, Salary = {d.basic_salary},  Language = {d.programming_language}')
print(f'Designe   = {de.name},Salary = {de.basic_salary}, Tool = {de.design_tool}')
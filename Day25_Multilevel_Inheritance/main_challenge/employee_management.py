print('===================================================================')
print('                 Employee Management System                        ')
print('===================================================================')


# Parent Class
class Person:

    # Initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Child Class inheriting Person
class Employee(Person):

    # Initialize employee details
    def __init__(self, name, age, employee_id, basic_salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.basic_salary = basic_salary


# Grandchild Class inheriting Employee
class Manager(Employee):

    # Initialize manager details
    def __init__(self, name, age, employee_id,
                 basic_salary, department, bonus):
        super().__init__(name, age, employee_id, basic_salary)
        self.department = department
        self.bonus = bonus

    # Calculate annual salary
    # Formula = (Monthly Salary × 12) + Bonus
    def calculate_annual_salary(self):
        annual_salary = (self.basic_salary * 12) + self.bonus
        return annual_salary

    # Display complete manager information
    def display(self):
        print(f'Name            : {self.name}')
        print(f'Age             : {self.age}')
        print(f'Employee ID     : {self.employee_id}')
        print(f'Basic Salary    : ₹{self.basic_salary}')
        print(f'Department      : {self.department}')
        print(f'Bonus           : ₹{self.bonus}')
        print(f'Annual Salary   : ₹{self.calculate_annual_salary()}')


# Create Manager Object
s = Manager(
    'Rahul',
    30,
    101,
    50000,
    'AI & ML',
    10000
)

print()
print('========== MANAGER DETAILS ==========')
print()

# Display manager details
s.display()
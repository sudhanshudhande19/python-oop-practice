# ===========================================================
#               EMPLOYEE MANAGEMENT SYSTEM
# ===========================================================

# Parent Class
class Person:

    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display person details
    def display_person(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')


# Child Class of Person
class Employee(Person):

    # Constructor
    def __init__(self, name, age, employee_id, salary):
        # Call Parent Class Constructor
        super().__init__(name, age)

        # Employee-specific attributes
        self.employee_id = employee_id
        self.salary = salary

    # Display employee details
    def display_employee(self):
        print(f'Employee ID = {self.employee_id}')
        print(f'Salary = {self.salary}')

    # Calculate annual salary
    def calculate_annual_salary(self):
        print(f'Annual Salary = {self.salary * 12}')


# Child Class of Employee
class Manager(Employee):

    # Constructor
    def __init__(self, name, age, employee_id, salary, department, bonus):

        # Call Employee Constructor
        super().__init__(name, age, employee_id, salary)

        # Manager-specific attributes
        self.department = department
        self.bonus = bonus

    # Calculate total salary including bonus
    def calculate_total_salary(self):
        print(f'Total Salary = {self.salary + self.bonus}')

    # Display manager details
    def display_manager(self):
        print(f'Department = {self.department}')
        print(f'Bonus = {self.bonus}')


# ===========================================================
#                   EMPLOYEE DETAILS
# ===========================================================

print('===== EMPLOYEE MANAGEMENT SYSTEM =====')

# Create Employee Object
e = Employee('Rahul', 24, 'E101', 30000)

# Display Person Details
e.display_person()

# Display Employee Details
e.display_employee()

# Display Annual Salary
e.calculate_annual_salary()

print()


# ===========================================================
#                   MANAGER DETAILS
# ===========================================================

print('===== MANAGER DETAILS =====')
print()

# Create Manager Object
e1 = Manager('Amit', 30, 'M101', 50000, 'IT', 10000)

# Display Person Details
e1.display_person()

# Display Employee Details
e1.display_employee()

# Display Manager Details
e1.display_manager()

# Display Total Salary
e1.calculate_total_salary()
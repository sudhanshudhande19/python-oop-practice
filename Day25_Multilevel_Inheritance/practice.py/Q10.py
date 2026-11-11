# Concept: Constructor chaining using super().

# Requirements:

    # Create Person, Employee, and Manager classes.
    # Person initializes name and age.
    # Employee initializes employee ID and salary.
    # Manager initializes department.
    # Use super() to initialize parent attributes.
    # Display all information.

#---------------------------------------------------------------------------------------------------------------


class Person:

    def __init__(self,name,age):
        self.name = name 
        self.age = age

class employee(Person):

    def __init__(self, name, age,employee_id,salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

class manager(employee):

    def __init__(self, name, age, employee_id, salary,department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')
        print(f'Employee ID = {self.employee_id}')
        print(f'Salary = {self.salary}')
        print(f'Department = {self.department}')


s = manager(
    'sudhanshu dhande',
    22,
    1234,
    60000,
    'IT'
)
s.display()
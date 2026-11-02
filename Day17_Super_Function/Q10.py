# Create three classes:

    # Person
    # Employee
    # Developer

# Requirements:

    # Person stores name.
    # Employee stores salary.
    # Developer stores programming_language.
    # Use super() at every inheritance level.
    # Display all details

#--------------------------------------------------------------------------------------------------


class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language


d = Developer("Sudhanshu Dhande", 50000, "Python")

print(f"Name = {d.name}")
print(f"Salary = {d.salary}")
print(f"Programming Language = {d.programming_language}")
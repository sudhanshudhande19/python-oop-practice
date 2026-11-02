# Create an Employee class with:

    # name
    # salary

# Create a Manager class with:

    # department

# Use super() to initialize employee details.

#------------------------------------------------------------------------------------------------------------------------------------



class Employe:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


class Manager(Employe):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

e = Manager('Sudhanshu Dhande',90000,'IT')
print(f'Name = {e.name}')
print(f'Salary = {e.salary}')
print(f'department = {e.department}')
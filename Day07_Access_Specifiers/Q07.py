# Create an Employee class with:

    # name as a public attribute
    # _salary as a protected-by-convention attribute

# Create a method display_salary().
# Display the employee's name and salary.
#_-------------------------------------------------------------------------------------

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary

    def display_salary(self):
        print(f'Name = {self.name}\nSalary ={self._salary}')

obj = Employee('Sudhanshu Dhande',96300)
obj.display_salary()
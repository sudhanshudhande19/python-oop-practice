# Create an Employee class with:
    # name
    # __salary

 # Create methods:
    # get_salary()
    # set_salary(salary)
    # display_details()
    # Reject negative salary values.
#---------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = 0
        self.set_salary(salary)

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
            print("Salary updated successfully")
        else:
            print("Error: Salary cannot be negative")

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.get_salary())


# Create object
e1 = Employee("Sudhanshu", 30000)

e1.display_details()

print("--------------------")

# Update salary
e1.set_salary(35000)
e1.display_details()

print("--------------------")

# Try negative salary
e1.set_salary(-5000)
e1.display_details()

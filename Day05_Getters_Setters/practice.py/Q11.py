# Create an Employee class with:

    # _name
    # _salary
    # _department

# Requirements:

    # Create properties for all three attributes.
    # Name and department cannot be empty.
    # Salary cannot be negative.
    # Create three employee objects and test the properties.
#--------------------------------------------------------------------------------------


class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if new_name.strip():
            self._name = new_name
        else:
            print("Name Cannot Be Empty")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_department):
        if new_department.strip():
            self._department = new_department
        else:
            print("Department Cannot Be Empty")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0:
            self._salary = new_salary
        else:
            print("Salary Cannot Be Negative")

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("--------------------")


obj = Employee("Sudhanshu", 0, "AI")
obj2 = Employee("Kunal", 40000, "AI")
obj3 = Employee("Aditya", 30000, "CSE")

# Test the properties
obj.name = ""
obj2.salary = 60000
obj3.department = "Marketing"

obj.display()
obj2.display()
obj3.display()

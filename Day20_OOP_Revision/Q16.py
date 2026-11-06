# Create Person → Employee → Manager classes. Use super() at every inheritance level.

#---------------------------------------------------------------------------------------------------------


class Person:
    def __init__(self, name):
        self.name = name
        print("Person Constructor")


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id
        print("Employee Constructor")


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department
        print("Manager Constructor")

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


m = Manager("Sudhanshu", 101, "IT")
m.display()
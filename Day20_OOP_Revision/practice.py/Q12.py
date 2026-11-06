# Create Person → Employee → Developer classes.

#-------------------------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id


class Developer(Employee):
    def __init__(self, name, employee_id, language):
        super().__init__(name, employee_id)
        self.language = language

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Language:", self.language)


dev = Developer("Sudhanshu", 101, "Python")
dev.display()

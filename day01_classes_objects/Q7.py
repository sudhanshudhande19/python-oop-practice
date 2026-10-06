# Create an Employee class with (name,salary,department) Create three employee objects and display their details.

class Employee:
    name = ''
    salary =''
    department = ''

    def info(self):
        print(f'Name = {self.name}\nSalary = {self.salary}\nDepartment = {self.department}\n')


obj = Employee()
obj2 = Employee()

obj.name = 'Sudhanshu Dhande'
obj.salary = 80000
obj.department = 'AI'

obj2.name = 'Pranay Dhande'
obj2.salary = 100000
obj2.department = 'CSE'

obj.info()
obj2.info()      
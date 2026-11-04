# Create an Employee class with a constructor that accepts:

# 1.name
# 2.salary
# 3.department

# Create an object and display the employee details.
#--------------------------------------------------------------------------------

class employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def info(self):
        print(f'Name ={self.name}\nSalary ={self.salary}\nDepartemnt ={self.department}')

obj = employee('Sudhanshu Dhande',80000,'AI')
obj.info()    
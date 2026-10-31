# Create an Employee class with:

# employee_id
# name
# salary

# Display all instance attributes using __dict__.

#_---------------------------------------------------------------------------------------


class Employee:

    def __init__(self,employee_id,name,salary):
        self.Employee_id = employee_id
        self.Name = name
        self.Salary = salary


e1 = Employee(1012,'Sudhanshu Dhande',80000)
e2 = Employee(1013,'Kedar Hemane',40000)

print(e1.__dict__)
print(e2.__dict__)
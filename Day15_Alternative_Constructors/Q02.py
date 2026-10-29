# Create an Employee class with:

    # name
    # department
    # salary

# Requirements:

    # Create a class method from_string(data).
    # Accept data in the format "Amit,IT,35000".
    # Convert the salary into a numeric value.
    # Create and display the employee object.`

#---------------------------------------------------------------------------------------------------

class Employee:

    def __init__(self,name,department,salary):
        self.name = name
        self.department = department
        self.salary = salary


    @classmethod
    def from_string(cls,data):
        name ,department,salary = data.split(',')
        return cls(name, (department),int(salary))

e1 = Employee.from_string('Sudhanshu Dhande,IT,85000')
e2 = Employee.from_string('Kedar Hemane,Product,65000')

print(e1.name,e1.department,e1.salary)
print(e2.name,e2.department,e2.salary)
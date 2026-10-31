# Create an Employee class.

# Requirements:

    # Create two employee objects.
    # Display both __dict__ values.
    # Compare their stored data.
    # Identify which attributes are different.

#----------------------------------------------------------------------------------------


class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


e = Employee('Sudhanshu dhande',80000)
e1 = Employee('Kunal',50000)

print(e.__dict__)
print(e1.__dict__)
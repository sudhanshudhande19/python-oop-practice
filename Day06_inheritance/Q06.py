# Create a parent class Person with a constructor accepting:
    # name
    # age

# Create a child class Teacher with:
    # subject
    # salary

# Requirements:
    # Initialize the parent attributes.
    # Initialize the child attributes.
    # Use super() to call the parent constructor.
    # Display all details.
#------------------------------------------------------------------------------------


class person:
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def show(self):
        print(f'Name ={self.name}\nAge ={self.age}')

class teachaer(person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

e1 = teachaer('Sudhanshu Dhande',22,5,80000)
e1.show()
print('subject =',e1.subject)
print('Salary =',e1.salary)
    
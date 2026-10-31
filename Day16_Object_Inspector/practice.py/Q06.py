# Create a Student class with:

# name
# marks
# study()
# display()

# Use dir() to inspect the object.

#------------------------------------------------------------------------------------


class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def study(self):
        print(f"{self.name} is studying.")

    def display(self):
        print(f'Name = {self.name}')
        print(f'Marks = {self.marks}')

x = Student('sudhanshu',90)

x.study()
x.display()
print(dir(x))
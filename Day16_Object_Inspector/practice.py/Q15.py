# Create a Student class.

# Requirements:

    # Create an object.
    # Add attributes dynamically.
    # Display all stored attributes.
    # Use dir() to inspect available names.
    # Use help() to inspect the class.

#-------------------------------------------------------------------------------------------


class Student:

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

e = Student('Sudhanshu Dhande',22,90)

print(dir(e))
print(help(Student))
# Create a Student class with:

    # name
    # marks

# Requirements:

    # Create a regular constructor.
    # Create a class method from_string(data).
    # Accept data in the format "Rahul,85".
    # Split the string and create a Student object.
    # Display the student's details.

#----------------------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls,data):
        name , marks = data.split(',')
        return cls(name, int(marks))

s1 = Student.from_string('Sudhanhsu,85')
print(s1.name,s1.marks)
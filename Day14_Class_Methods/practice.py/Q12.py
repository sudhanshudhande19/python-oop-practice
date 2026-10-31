# Create a Student class with:

    # name
    # marks

# Requirements:

    # Create a regular constructor that accepts a name and marks.
    # Create a class method from_string(data).
    # Accept input in the format "Sudhanshu,85".
    # Split the input and return a new Student object.
    # Validate that marks are between 0 and 100.

#-----------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self,name,marks):
        self.name = name
        if  0 <= marks <= 100:
            self.marks = marks
        else:
            print("Enter The Correct Marks")
       
    @classmethod
    def from_string(cls,data):
        name,marks = data.split(',')
        return cls(name.strip(),int(marks))

s1 = Student('Sudhanshu',85)
print(s1.name, s1.marks)

s2 = Student.from_string("Sudhanshu,85")
print(s2.name, s2.marks)

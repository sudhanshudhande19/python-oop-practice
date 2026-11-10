# Create a Person class and a School class. Inherit both into a Student class.

# Concept: Combining Attributes from Multiple Parents.

# Requirements:

    # Person stores name and age.
    # School stores school name and location.
    # Student stores roll number and marks.
    # Student should access attributes from both parents.
    # Display all student details.

#-----------------------------------------------------------------------------------------------------------------------------------------


class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 

class School:
    def __init__(self,school_name,location):
        self.school_name = school_name 
        self.location = location

class Student(Person,School):

    def __init__(self, name, age,roll_no,marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

s = Student('Rahul',20,101,85)
l = School("DBATU",'Nagpur')

print(f'Name = {s.name}')
print(f'Age = {s.age}')
print(f'School Name = {l.school_name}')
print(f'Location = {l.location}')
print(f'Roll No = {s.roll_no}')
print(f'Marks = {s.marks}')
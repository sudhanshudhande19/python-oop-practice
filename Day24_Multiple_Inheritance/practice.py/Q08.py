# Create a Student class and a SportsPlayer class. Inherit both into a CollegeStudent class.

# Concept: Multiple Inheritance with Real-World Roles.

# Requirements:

    # Student stores name, roll number and marks.
    # SportsPlayer stores sport name and achievements.
    # CollegeStudent stores college name.
    # Access attributes from both parent classes.
    # Display academic and sports details.

#---------------------------------------------------------------------------------------------------------------------------


class Student:

    def __init__(self,name,roll_no,marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks

class sportplayer:

    def __init__(self,name,achievements):
        self.name  = name 
        self.achievements = achievements


class collegestudent(Student,sportplayer):

    def __init__(self, name, roll_no, marks,college_name):
        super().__init__(name, roll_no, marks)
        self.college_name = college_name


s = collegestudent('sudhanshu Dhande',101,90,'DBATU')
v = sportplayer('volleyboll',5)

print(f'Student Name = {s.name}')
print(f'Roll No      = {s.roll_no}')
print(f'marks        = {s.marks}')
print(f'Sport Name   = {v.name}')
print(f'Achievement  = {v.achievements}')
print(f'College Name = {s.college_name}')
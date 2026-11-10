# Create Student, SportsPlayer and Researcher parent classes. Inherit all three into a UniversityStudent class.

# Concept: Multiple Inheritance with Three Parent Classes.

# Requirements:

    # Student stores name, roll number and marks.
    # SportsPlayer stores sport and achievements.
    # Researcher stores research topic and publication count.
    # UniversityStudent stores university name.
    # Access all parent attributes.
    # Display complete student information.

#------------------------------------------------------------------------------------------------------

class Student:

    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

class sportplayer:
    def __init__(self,sport_name,achievement):
        self.sport_name = sport_name
        self.achievement = achievement

class Researcher:
    def __init__(self,research_topic,pub_count):
        self.research_topic = research_topic
        self.pub_count = pub_count

class UniversityStudent(Student,sportplayer,Researcher):

    def __init__(self, name, roll_no, marks,university_name):
        super().__init__(name, roll_no, marks)
        self.university_name = university_name

s = UniversityStudent('Sudhanshu Dhande',101,90,'DBATU')
x = sportplayer('Volleyboll',5)
c = Researcher('Human Body',2)

print(f'University Name = {s.university_name}')
print(f'Student Name = {s.name}')
print(f'Roll No = {s.roll_no}')
print(f'Marks = {s.marks}')
print(f'Sports Name = {x.sport_name}')
print(f'Achievement = {x.achievement}')
print(f'Research Topic = {c.research_topic}')
print(f'Publication Count = {c.pub_count}')

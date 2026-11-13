# Concept: Hybrid Inheritance with academic details.

# Requirements:

    # Create University as parent.
    # Student and Professor inherit from University.
    # ResearchStudent inherits from Student and Professor.
    # University stores university name.
    # Student stores roll number.
    # Professor stores department.
    # ResearchStudent stores research topic.
    # Display all details.
    # Check the MRO.

#--------------------------------------------------------------------------------------------------------


class University:

    def __init__(self,name):
        self.name = name

class Student(University):

    def __init__(self, name,roll_no):
        University.__init__(self,name)
        self.roll_no = roll_no

class Prodessor(University):
    def __init__(self,name,department):
        University.__init__(self,name)
        self.department = department

class ResearchStudent(Student,Prodessor):

    def __init__(self, name,roll_no,department,research_topic):
        Student.__init__(self,name, roll_no)
        Prodessor.__init__(self,name,department)
        self.research_topic = research_topic


s = ResearchStudent('DBATU University',101,'Computer Science','Artificial Intelligence')
print(f'University = {s.name}')
print(f'Roll Number = {s.roll_no}')
print(f'department = {s.department}')
print(f'Research Topic = {s.research_topic}')

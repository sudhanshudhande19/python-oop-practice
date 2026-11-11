# Concept: Multilevel Inheritance with organizational structure.

# Requirements:

    # Create School, Department, and Teacher classes.
    # School stores school name.
    # Department stores department name.
    # Teacher stores teacher name and subject.
    # Display all details.


#_----------------------------------------------------------------------------------------------------

class School:

    def __init__(self,school_name):
        self.school_name = school_name

class Department(School):

    def __init__(self, school_name,department):
        super().__init__(school_name)
        self.department = department

class Teacher(Department):

    def __init__(self, school_name, department,teacher_name,subject):
        super().__init__(school_name, department)
        self.teacher_name = teacher_name
        self.subject = subject

    def display(self):
        print(f'School Name  = {self.school_name}')
        print(f'Department   = {self.department}')
        print(f'Teacher Name = {self.teacher_name}')
        print(f'Subject      = {self.subject}')

s = Teacher('KCEM','AI','Sudhanshu','python')
s.display()
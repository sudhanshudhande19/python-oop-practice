print('================================================================')
print('                    College Management System                   ')
print('================================================================')


# Parent Class
class Person:
    # Class Variable
    college = 'Karenjekar College of Engineering And Management.'

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Display Person Details
    def display_detail(self):
        print(f'Name = {self.name}')
        print(f'Age = {self.age}')


# Student Class inherits Person
class Student(Person):

    def __init__(self, name, age, roll_number, marks):
        # Call Parent Constructor
        super().__init__(name, age)

        # Marks Validation
        if not (0 <= marks <= 100):
            raise ValueError("Marks must be between 0 and 100")

        self.roll_number = roll_number
        self.marks = marks

    # Calculate Grade
    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'

    # Method Overriding
    def display_detail(self):
        super().display_detail()
        print(f'Roll No = {self.roll_number}')
        print(f'Marks = {self.marks}')
        print(f'Grade = {self.calculate_grade()}')
        print('----------------------------------------')


# Teacher Class inherits Person
class Teacher(Person):

    def __init__(self, name, age, teacher_id, subject):
        # Call Parent Constructor
        super().__init__(name, age)

        self.teacher_id = teacher_id
        self.subject = subject

    # Method Overriding
    def display_detail(self):
        super().display_detail()
        print(f'Teacher ID = {self.teacher_id}')
        print(f'Subject = {self.subject}')
        print('------------------------------------')


# College Class
class College:

    # Constructor
    def __init__(self, college_name):
        self.college_name = college_name
        self.student = []   # List to store students
        self.teacher = []   # List to store teachers

    # Add Student Object
    def add_student(self, student):
        self.student.append(student)

    # Add Teacher Object
    def add_teacher(self, teacher):
        self.teacher.append(teacher)

    # Display All Students
    def display_student(self):
        print('\nStudents')
        for stu in self.student:
            stu.display_detail()

    # Display All Teachers
    def display_teacher(self):
        print('\nTeachers')
        for tea in self.teacher:
            tea.display_detail()

    # Display Complete College Information
    def display_college_info(self):
        print('\nCollege Name =', self.college_name)

        self.display_student()
        self.display_teacher()

    def list_len(self):
        print(f'Total Student = {len(self.student)}')
        print(f'Total Teacher = {len(self.teacher)}')

# Create Student Objects
s1 = Student("Sudhanshu", 21, 101, 88)
s2 = Student("Rahul", 22, 102, 95)

# Create Teacher Object
t1 = Teacher("Patil Sir", 40, "T101", "Python")

# Create College Object
college = College("Karanjekar College of Engineering and Management")

# Add Students to College
college.add_student(s1)
college.add_student(s2)

# Add Teacher to College
college.add_teacher(t1)

# Display Complete Information
college.display_college_info()

college.list_len()
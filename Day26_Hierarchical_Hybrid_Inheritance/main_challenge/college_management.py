print("===================================================")
print("              College Management System            ")
print("===================================================")


class College:

    def __init__(self, college_name, location):
        self.college_name = college_name
        self.location = location


class Student(College):

    def __init__(self, college_name, location, name, roll_no, marks):
        College.__init__(self, college_name, location)
        self.name = name
        self.roll_no = roll_no
        self.marks = marks


class Teacher(College):

    def __init__(self, college_name, location, teacher_name, subject, salary):
        College.__init__(self, college_name, location)
        self.teacher_name = teacher_name
        self.subject = subject
        self.salary = salary


class TeachingAssistant(Student, Teacher):

    def __init__(self, college_name, location, name, roll_no,
                 marks, teacher_name, subject, salary, assistant_id):

        Student.__init__(self, college_name, location, name, roll_no, marks)
        Teacher.__init__(self, college_name, location, teacher_name, subject, salary)

        self.assistant_id = assistant_id

    def info(self):
        print("\n-------------------------------")
        print(f"College Name   : {self.college_name}")
        print(f"Location       : {self.location}")

        print("\n----- Student Details -----")
        print(f"Student Name   : {self.name}")
        print(f"Roll Number    : {self.roll_no}")
        print(f"Marks          : {self.marks}")

        print("\n----- Teacher Details -----")
        print(f"Teacher Name   : {self.teacher_name}")
        print(f"Subject        : {self.subject}")
        print(f"Salary         : {self.salary}")

        print("\n----- TA Details -----")
        print(f"Assistant ID   : {self.assistant_id}")
        print("-------------------------------")


# Object 1
s = TeachingAssistant(
    "KCEM",
    "Sakoli",
    "Sudhanshu",
    101,
    85,
    "Amit",
    "Python",
    40000,
    "TA01"
)

# Object 2
t = TeachingAssistant(
    "KCEM",
    "Sakoli",
    "Ayush",
    105,
    75,
    "Priya",
    "Java",
    30000,
    "TA02"
)

s.info()
t.info()
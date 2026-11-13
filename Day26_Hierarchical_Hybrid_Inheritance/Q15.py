# Concept: Advanced Hybrid Inheritance.

# Requirements:

    # Create College as the common parent class.
    # Create Student and Teacher child classes.
    # Create TeachingAssistant inheriting from Student and Teacher.
    # College stores college name and location.
    # Student stores roll number and marks.
    # Teacher stores subject and salary.
    # TeachingAssistant stores assistant ID.
    # Use constructors and super().
    # Display all inherited information.
    # Print the MRO.
    # Create at least two TeachingAssistant objects.


#-------------------------------------------------------------------------------------------------------------
class College:
    def __init__(self, college_name, location):
        self.college_name = college_name
        self.location = location


class Student(College):
    def __init__(self, college_name, location, roll_number, marks):
        College.__init__(self, college_name, location)
        self.roll_number = roll_number
        self.marks = marks


class Teacher(College):
    def __init__(self, college_name, location, subject, salary):
        College.__init__(self, college_name, location)
        self.subject = subject
        self.salary = salary


class TeachingAssistant(Student, Teacher):
    def __init__(self, college_name, location,
                 roll_number, marks,
                 subject, salary, assistant_id):

        Student.__init__(
            self, college_name, location,
            roll_number, marks
        )

        Teacher.__init__(
            self, college_name, location,
            subject, salary
        )

        self.assistant_id = assistant_id

    def display(self):
        print("College Name:", self.college_name)
        print("Location:", self.location)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("Subject:", self.subject)
        print("Salary:", self.salary)
        print("Assistant ID:", self.assistant_id)
        print("-" * 30)


ta1 = TeachingAssistant(
    "ABC College", "Nagpur",
    101, 88,
    "Python", 25000,
    "TA001"
)

ta2 = TeachingAssistant(
    "ABC College", "Nagpur",
    102, 92,
    "Data Science", 30000,
    "TA002"
)

ta1.display()
ta2.display()

print("MRO:")
for cls in TeachingAssistant.mro():
    print(cls.__name__)
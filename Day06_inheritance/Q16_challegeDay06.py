
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)

    def introduce(self):
        print(f"I am {self.name}, aged {self.age}.")

    
class Student(Person):
    def __init__(self, name, age, city, roll_number, branch, marks):
        super().__init__(name, age, city)
        self.roll_number = roll_number
        self.branch = branch
        self.marks = marks

    def display_student(self):
        self.display_person()
        print("Roll Number:", self.roll_number)
        print("Branch:", self.branch)
        print("Marks:", self.marks)
        print("Percentage:", self.calculate_percentage(), "%")
        self.check_result()

    def calculate_percentage(self):
        # Assuming marks are out of 100 in 5 subjects
        total_marks = sum(self.marks)
        maximum_marks = len(self.marks) * 100
        return round((total_marks / maximum_marks) * 100, 2)

    def check_result(self):
        percentage = self.calculate_percentage()

        if percentage >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")

    # Method overriding
    def introduce(self):
        print(
            f"I am {self.name}, a student of {self.branch}."
        )


class Teacher(Person):
    def __init__(self, name, age, city, employee_id, subject, salary):
        super().__init__(name, age, city)
        self.employee_id = employee_id
        self.subject = subject
        self.salary = salary

    def display_teacher(self):
        self.display_person()
        print("Employee ID:", self.employee_id)
        print("Subject:", self.subject)
        print("Monthly Salary: ₹", self.salary)
        print("Annual Salary: ₹", self.annual_salary())

    def annual_salary(self):
        return self.salary * 12

    # Method overriding
    def introduce(self):
        print(
            f"I am {self.name}, a teacher of {self.subject}."
        )


# Three student objects
s1 = Student(
    "Sudhanshu", 22, "Sakoli",
    101, "Artificial Intelligence",
    [85, 78, 90, 88, 92]
)

s2 = Student(
    "Kunal", 21, "Nagpur",
    102, "Computer Science",
    [65, 72, 58, 80, 75]
)

s3 = Student(
    "Rahul", 22, "Pune",
    103, "Information Technology",
    [30, 35, 42, 38, 25]
)


# Two teacher objects
t1 = Teacher(
    "Amit Sharma", 40, "Nagpur",
    "T101", "Python", 50000
)

t2 = Teacher(
    "Priya Verma", 35, "Pune",
    "T102", "Machine Learning", 60000
)


# Display student details
print("========== STUDENT 1 ==========")
s1.display_student()
s1.introduce()

print("\n========== STUDENT 2 ==========")
s2.display_student()
s2.introduce()

print("\n========== STUDENT 3 ==========")
s3.display_student()
s3.introduce()


# Display teacher details
print("\n========== TEACHER 1 ==========")
t1.display_teacher()
t1.introduce()

print("\n========== TEACHER 2 ==========")
t2.display_teacher()
t2.introduce()

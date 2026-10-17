class Person:
    college_name = "ABC College"

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_person(self):
        print(f"College : {Person.college_name}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"City    : {self.city}")

    @classmethod
    def update_college_name(cls, new_name):
        cls.college_name = new_name


class Student(Person):
    def __init__(self, name, age, city,
                 roll_number, branch, marks):
        super().__init__(name, age, city)

        self.roll_number = roll_number
        self.branch = branch

        if self.validate_marks(marks):
            self.__marks = marks
        else:
            self.__marks = [0, 0, 0]

    def validate_marks(self, marks):
        return (
            len(marks) == 3 and
            all(0 <= mark <= 100 for mark in marks)
        )

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if self.validate_marks(marks):
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks! Marks must be between 0 and 100.")

    def calculate_percentage(self):
        return sum(self.__marks) / len(self.__marks)

    def check_result(self):
        if all(mark >= 35 for mark in self.__marks):
            return "PASS"
        return "FAIL"

    def display_student(self):
        print("\n===== STUDENT DETAILS =====")
        self.display_person()
        print(f"Roll No : {self.roll_number}")
        print(f"Branch  : {self.branch}")
        print(f"Marks   : {self.__marks}")
        print(f"Percent : {self.calculate_percentage():.2f}%")
        print(f"Result  : {self.check_result()}")
        print("-" * 35)


class Teacher(Person):
    def __init__(self, name, age, city,
                 employee_id, subject, monthly_salary):
        super().__init__(name, age, city)

        self.employee_id = employee_id
        self.subject = subject
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

    def display_teacher(self):
        print("\n===== TEACHER DETAILS =====")
        self.display_person()
        print(f"Employee ID    : {self.employee_id}")
        print(f"Subject        : {self.subject}")
        print(f"Monthly Salary : {self.monthly_salary}")
        print(f"Annual Salary  : {self.annual_salary()}")
        print("-" * 35)


# ----------------------------
# Create Students
# ----------------------------

s1 = Student(
    "Sudhanshu", 21, "Sangamner",
    101, "Computer", [85, 90, 80]
)

s2 = Student(
    "Rahul", 20, "Pune",
    102, "Mechanical", [40, 30, 50]
)

s3 = Student(
    "Priya", 22, "Nashik",
    103, "IT", [70, 75, 82]
)
# ----------------------------
# Create Teachers
# ----------------------------

t1 = Teacher(
    "Sharma Sir", 45, "Pune",
    "T101", "Python", 50000
)

t2 = Teacher(
    "Patil Madam", 40, "Nashik",
    "T102", "Database", 55000
)


# ----------------------------
# Display Data
# ----------------------------

s1.display_student()
s2.display_student()
s3.display_student()

t1.display_teacher()
t2.display_teacher()


# ----------------------------
# Class Method Demo
# ----------------------------

Person.update_college_name("Deloitte Institute")

print("\nUpdated College Name:")
s1.display_person()
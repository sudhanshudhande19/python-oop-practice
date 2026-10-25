
class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")


class Student(Person):
    def __init__(self, name, age, city, roll_number, branch, marks):
        super().__init__(name, age, city)

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")

        self.roll_number = roll_number
        self.branch = branch
        self.marks = marks

    def calculate_percentage(self):
        # Marks are out of 100
        return self.marks

    def check_result(self):
        if self.calculate_percentage() >= 40:
            return "Pass"
        return "Fail"

    def display_details(self):
        print("\n--- Student Details ---")
        super().display_details()
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")
        print(f"Marks: {self.marks}")
        print(f"Percentage: {self.calculate_percentage()}%")
        print(f"Result: {self.check_result()}")


class Teacher(Person):
    def __init__(
        self, name, age, city, employee_id, subject, monthly_salary
    ):
        super().__init__(name, age, city)

        if monthly_salary < 0:
            raise ValueError("Salary cannot be negative.")

        self.employee_id = employee_id
        self.subject = subject
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self):
        return self.monthly_salary * 12

    def display_details(self):
        print("\n--- Teacher Details ---")
        super().display_details()
        print(f"Employee ID: {self.employee_id}")
        print(f"Subject: {self.subject}")
        print(f"Monthly Salary: Rs. {self.monthly_salary}")
        print(f"Annual Salary: Rs. {self.calculate_annual_salary()}")


# Separate lists for storing objects
students = []
teachers = []


def add_student():
    try:
        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        city = input("Enter city: ")
        roll_number = int(input("Enter roll number: "))
        branch = input("Enter branch: ")
        marks = float(input("Enter marks (0-100): "))

        if any(s.roll_number == roll_number for s in students):
            print("Error: Roll number already exists.")
            return

        student = Student(
            name, age, city, roll_number, branch, marks
        )
        students.append(student)
        print("Student added successfully!")

    except ValueError as error:
        print("Invalid input:", error)


def display_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        student.display_details()


def add_teacher():
    try:
        name = input("Enter teacher name: ")
        age = int(input("Enter age: "))
        city = input("Enter city: ")
        employee_id = int(input("Enter employee ID: "))
        subject = input("Enter subject: ")
        monthly_salary = float(input("Enter monthly salary: "))

        if any(t.employee_id == employee_id for t in teachers):
            print("Error: Employee ID already exists.")
            return

        teacher = Teacher(
            name, age, city, employee_id, subject, monthly_salary
        )
        teachers.append(teacher)
        print("Teacher added successfully!")

    except ValueError as error:
        print("Invalid input:", error)


def display_teachers():
    if not teachers:
        print("No teachers found.")
        return

    for teacher in teachers:
        teacher.display_details()


def search_student():
    try:
        roll_number = int(input("Enter roll number to search: "))

        for student in students:
            if student.roll_number == roll_number:
                student.display_details()
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid roll number.")


def main():
    # Initial sample data: 3 students and 2 teachers
    students.extend([
        Student("Sudhanshu Dhande", 22, "Sakoli", 101, "AI", 54),
        Student("Kedar Hemane", 22, "Sakoli", 102, "AI", 40),
        Student("Ayush Gharde", 22, "Sakoli", 103, "AI", 88)
    ])

    teachers.extend([
        Teacher("Amit Sharma", 40, "Sakoli", 1121, "Python", 50000),
        Teacher("Neha Patil", 35, "Nagpur", 1122, "Java", 40000)
    ])

    while True:
        print("\n===== College Management System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Add Teacher")
        print("4. Display Teachers")
        print("5. Search Student by Roll Number")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            add_teacher()

        elif choice == "4":
            display_teachers()

        elif choice == "5":
            search_student()

        elif choice == "6":
            print("Exiting College Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1 to 6.")


if __name__ == "__main__":
    main()

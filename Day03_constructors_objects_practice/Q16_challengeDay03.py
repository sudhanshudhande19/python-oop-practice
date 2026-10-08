#College Student Management
#------------------------------------------------------------------
class Student:
    def __init__(self, name, roll_number, branch, year, marks):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch
        self.year = year
        self.marks = marks

    def display_details(self):
        print(f"Name        : {self.name}")
        print(f"Roll No     : {self.roll_number}")
        print(f"Branch      : {self.branch}")
        print(f"Year        : {self.year}")
        print(f"Marks       : {self.marks}")
        print(f"Total Marks : {self.total_marks()}")
        print(f"Percentage  : {self.percentage():.2f}%")
        print(f"Grade       : {self.grade()}")
        print(f"Result      : {self.result()}")
        print("-" * 40)

    def total_marks(self):
        return sum(self.marks)

    def percentage(self):
        return (self.total_marks() / (len(self.marks) * 100)) * 100

    def grade(self):
        per = self.percentage()

        if per >= 90:
            return "A+"
        elif per >= 80:
            return "A"
        elif per >= 70:
            return "B"
        elif per >= 60:
            return "C"
        elif per >= 50:
            return "D"
        else:
            return "F"

    def result(self):
        if self.percentage() >= 40:
            return "Pass"
        return "Fail"

    def is_topper(self, highest_percentage):
        return self.percentage() == highest_percentage


# Create Students
s1 = Student("Sudhanshu", 101, "CSE", 3, [80, 90, 85, 88, 92])
s2 = Student("Priya", 102, "IT", 3, [75, 78, 82, 80, 85])
s3 = Student("Rahul", 103, "CSE", 2, [60, 65, 70, 72, 68])
s4 = Student("Anjali", 104, "ECE", 1, [95, 92, 98, 96, 99])
s5 = Student("Kunal", 105, "ME", 4, [35, 40, 38, 42, 36])

students = [s1, s2, s3, s4, s5]

# Display all students
for student in students:
    student.display_details()

# Highest Percentage Student
highest = max(students, key=lambda s: s.percentage())

# Lowest Percentage Student
lowest = min(students, key=lambda s: s.percentage())

# Average Percentage of Class
avg_percentage = sum(s.percentage() for s in students) / len(students)

# Pass/Fail Count
pass_count = sum(1 for s in students if s.result() == "Pass")
fail_count = sum(1 for s in students if s.result() == "Fail")

print("\nCLASS REPORT")
print("=" * 40)

print(
    f"Highest Percentage : {highest.name} "
    f"({highest.percentage():.2f}%)"
)

print(
    f"Lowest Percentage  : {lowest.name} "
    f"({lowest.percentage():.2f}%)"
)

print(f"Average Percentage : {avg_percentage:.2f}%")
print(f"Students Passed    : {pass_count}")
print(f"Students Failed    : {fail_count}")

print("\nTOPPER CHECK")
for student in students:
    if student.is_topper(highest.percentage()):
        print(f"{student.name} is the Topper")
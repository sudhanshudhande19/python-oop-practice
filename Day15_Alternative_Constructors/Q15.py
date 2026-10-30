# Create a Student class with:

    # name
    # roll_number
    # marks

# Requirements:

    # Create a regular constructor.
    # Create from_string(data).
    # Create from_dict(data).
    # Create from_list(data).
    # Use all four methods to create student objects.
    # Display and compare their details.
    # Validate the data consistently across all constructors.

#-----------------------------------------------------------------------------------------------------------

class Student:

    def __init__(self, name, roll_number, marks):

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")

        if not isinstance(roll_number, int) or isinstance(roll_number, bool) or roll_number <= 0:
            raise ValueError("Roll number must be a positive integer")

        if not isinstance(marks, (int, float)) or isinstance(marks, bool):
            raise ValueError("Marks must be numeric")

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")

        self.name = name.strip()
        self.roll_number = roll_number
        self.marks = marks

    # 1. Alternative constructor using String
    @classmethod
    def from_string(cls, data):

        parts = data.split(",")

        if len(parts) != 3:
            raise ValueError("Format: Name,Roll_Number,Marks")

        name, roll_number, marks = parts

        try:
            return cls(
                name.strip(),
                int(roll_number.strip()),
                float(marks.strip())
            )
        except ValueError as error:
            raise ValueError(f"Invalid string data: {error}")

    # 2. Alternative constructor using Dictionary
    @classmethod
    def from_dict(cls, data):

        try:
            return cls(
                data["name"],
                data["roll_number"],
                data["marks"]
            )
        except KeyError as error:
            raise ValueError(f"Missing field: {error}")

    # 3. Alternative constructor using List
    @classmethod
    def from_list(cls, data):

        if not isinstance(data, (list, tuple)) or len(data) != 3:
            raise ValueError("List must contain name, roll_number, marks")

        return cls(data[0], data[1], data[2])

    # Display student details
    def display(self):

        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_number}")
        print(f"Marks       : {self.marks}")
        print("-" * 35)


# 1. Regular Constructor
s1 = Student("Sudhanshu", 101, 85)

# 2. String Constructor
s2 = Student.from_string("Kunal,102,90")

# 3. Dictionary Constructor
s3 = Student.from_dict({
    "name": "Kedar",
    "roll_number": 103,
    "marks": 78
})

# 4. List Constructor
s4 = Student.from_list(["Aditya", 104, 88])


# Display all students
students = [s1, s2, s3, s4]

print("STUDENT DETAILS")
for student in students:
    student.display()


# Compare student details
print("\nSTUDENT COMPARISON")

for student in students:
    print(
        f"{student.name} | "
        f"Roll No: {student.roll_number} | "
        f"Marks: {student.marks}"
    )


# Test invalid input
print("\nINVALID INPUT TEST")

try:
    s5 = Student.from_string("Rahul,105,150")
except ValueError as error:
    print("Error:", error)

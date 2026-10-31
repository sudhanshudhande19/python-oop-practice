# Create a Student class with:

    # name
    # roll_number
    # marks

# Requirements:

    # Create a class method from_dict(data).
    # Accept a dictionary containing the student's details.
    # Create and return a Student object.
    # Display all details.

#--------------------------------------------------------------------------------------------------------------------

class  Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    @classmethod
    def from_dict(cls, data):
            return cls(
                data["name"],
                data["roll_number"],
                data["marks"]
            )

e1 = Student.from_dict({ "name": "Sudhanshu",
                        "roll_number": 101,
                        "marks": 85})

print(f"Name = {e1.name}")
print(f"Roll Number = {e1.roll_no}")
print(f"Marks = {e1.marks}")
# Improve your Student class.

# Requirements:

    # Store name, roll_number, and marks.
    # Create from_string(data).
    # Accept data in the format "Rahul,101,85".
    # Reject empty names.
    # Reject marks outside the range 0–100.
    # Handle invalid numeric input.
    # Create an object only when the input is valid.

#-----------------------------------------------------------------------------------------------------


class Student:

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    @classmethod
    def from_string(cls, data):
        try:
            name, roll_number, marks = data.split(',')

            name = name.strip()

            if not name:
                print("Reject Empty Name")
                return None

            roll_number = int(roll_number)
            marks = int(marks)

            if roll_number < 0:
                print("Invalid Roll Number")
                return None

            if marks < 0 or marks > 100:
                print("Reject Marks")
                return None

            return cls(name, roll_number, marks)

        except ValueError:
            print("Invalid Numeric Input")
            return None


e1 = Student.from_string('Rahul,101,85')

if e1:
    print(f'Name = {e1.name}')
    print(f'Roll Number = {e1.roll_number}')
    print(f'Marks = {e1.marks}')
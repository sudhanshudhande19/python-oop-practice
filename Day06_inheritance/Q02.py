# Create a parent class Person with:
    # name
    # age
    # display_person()

# Create a child class Student with:
    # roll_number
    # display_student()

# Display the person's and student's details.
#---------------------------------------------------------------------------------------


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number

    def display_student(self):
        print(f"Roll Number = {self.roll_number}")


e1 = Person("Sudhanshu", 22)
e1.display_person()

print("------------------")

e2 = Student("Kunal", 20, 23)
e2.display_person()
e2.display_student()

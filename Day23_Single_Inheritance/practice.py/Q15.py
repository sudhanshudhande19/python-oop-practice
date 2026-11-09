# Create a Person parent class and a Doctor child class.

# Concept: Complete Single Inheritance.

# Requirements:

    # Parent stores name and age.
    # Child stores doctor ID and specialization.
    # Use super() in the constructor.
    # Override the display method.
    # Call the parent display method using super().
    # Display complete doctor details.

#_---------------------------------------------------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):
    def __init__(self, name, age, doctor_id, specialization):
        super().__init__(name, age)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display(self):
        super().display()  
        print("Doctor ID:", self.doctor_id)
        print("Specialization:", self.specialization)


doctor1 = Doctor("Sudhanshu", 22, "D101", "Cardiologist")

doctor1.display()
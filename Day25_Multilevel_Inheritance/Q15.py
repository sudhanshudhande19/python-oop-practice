# Concept: Complete Multilevel Inheritance.

# Requirements:

    # Create Hospital, Department, and Doctor classes.
    # Hospital stores hospital name and location.
    # Department stores department name.
    # Doctor stores doctor name, specialization, and consultation fee.
    # Use constructors and super().
    # Create a method to display the complete doctor profile.
    # Create an object of Doctor and display all information.

#_--------------------------------------------------------------------------------------------------------------


class Hospital:
    def __init__(self, hospital_name, location):
        self.hospital_name = hospital_name
        self.location = location


class Department(Hospital):
    def __init__(self, hospital_name, location, department_name):
        super().__init__(hospital_name, location)
        self.department_name = department_name


class Doctor(Department):
    def __init__(self, hospital_name, location, department_name,doctor_name, specialization, consultation_fee):
        super().__init__(hospital_name, location, department_name)
        self.doctor_name = doctor_name
        self.specialization = specialization
        self.consultation_fee = consultation_fee

    def display_profile(self):
        print("Hospital Name:", self.hospital_name)
        print("Location:", self.location)
        print("Department:", self.department_name)
        print("Doctor Name:", self.doctor_name)
        print("Specialization:", self.specialization)
        print("Consultation Fee: ₹", self.consultation_fee)



doctor1 = Doctor(
    "Apollo Hospital",
    "Nagpur",
    "Cardiology",
    "Dr. Sharma",
    "Heart Specialist",
    1200
)

doctor1.display_profile()
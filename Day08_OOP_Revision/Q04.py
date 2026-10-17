# Create a Student class with the class attribute:
    # school_name = "BATU"

# Requirements:
    # Create three student objects.
    # Display the school name using all three objects.
    # Change the class attribute and observe the result.
    # Override the school name for only one object and observe what happens to the others.

#------------------------------------------------------------------------------------------------------------

class Student:
  
    school_name = 'DBATU'

    def display(self):
        print(f'School Name ={self.school_name}')
e = Student()
e2 = Student()
e3 = Student()

e.display()
e2.display = 'karanjekar college of engineering sakoli'
e3.display()

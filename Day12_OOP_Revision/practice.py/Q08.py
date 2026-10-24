# Create a Student class with a private attribute __marks.

# Requirements:

    # Create a getter using @property.
    # Create a setter using @marks.setter.
    # Accept marks only between 0 and 100.
    # Test valid and invalid values.

#-----------------------------------------------------------------------------------

class Student:

    def __init__(self):
        self.__marks = 55


    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self,new_marks):
        if 0<= new_marks <= 100:
            self.__marks = new_marks
            print('Valid Marks =',new_marks)
            
        else:
            print('Invalid Marks =',new_marks)

s1 = Student()


s1.marks = 95     # Setter


s1.marks = 120    # Invalid

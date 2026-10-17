# Create a Student class with:
    # name
    # _marks

# Requirements:
    # Use @property to read marks.
    # Use @marks.setter to update marks.
    # Accept marks only between 0 and 100.
    # Test valid and invalid values.

#------------------------------------------------------------------------
class Student:
    def __init__(self,name,_marks):
        self.name = name
        self._marks = _marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,new_marks):
        if 0 <= new_marks <= 100:
            self._marks = new_marks
            print('Valid Marks')
        else:
            print('Invalid Marks')
e = Student('sudhanshu',96)
print('Name = ',e.name)

e.marks =99
print('Marks =',e.marks)


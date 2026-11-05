# Create a College class with a college_info() method. Override it in Student and display both parent and child information.

#---------------------------------------------------------------------------------------------------------------------------------------------


class College:

    def college_info(self):
        print(f'College Name = Karanjekar College of Engineering and Management')
        print(f'place = Sakoli')
        print(f'college code = 4679')

class Student(College):

    def college_info(self):
        super().college_info()
        print(f'Student Name= Sudhanshu dhande')
        print(f'Age = 22')
        print(f'Mobile No = 9623711369')

s = Student()
s.college_info()
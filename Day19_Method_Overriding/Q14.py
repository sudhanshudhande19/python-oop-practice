# Create a parent class LibraryUser with a get_access() method. Override it in Student and Teacher with different access permissions.
#--------------------------------------------------------------------------------------------------------------------------------------------------------


class LibraryUser:
    def get_access(self):
        print("Library access granted")


class Student(LibraryUser):
    def get_access(self):
        print("Student Access: Can borrow 2 books and access the reading room")


class Teacher(LibraryUser):
    def get_access(self):
        print("Teacher Access: Can borrow 10 books and access all library resources")


s = Student()
t = Teacher()

s.get_access()
t.get_access()
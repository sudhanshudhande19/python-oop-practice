#Create a parent class Employee with a work() method. Override it in Developer.
#-------------------------------------------------------------------------------------------------------------------------


class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is writing code")


e= Employee()
d = Developer()
e.work()
d.work()
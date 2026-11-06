# Create Father and Mother classes. Inherit both into a Child class.


#----------------------------------------------------------------------------------------
class Father:
    def father_quality(self):
        print("Father's quality: Hardworking")


class Mother:
    def mother_quality(self):
        print("Mother's quality: Caring")


class Child(Father, Mother):
    def child_quality(self):
        print("Child inherits qualities from both parents")


c = Child()
c.father_quality()
c.mother_quality()
c.child_quality()
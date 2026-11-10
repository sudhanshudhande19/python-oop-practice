# Create a Father class and a Mother class. Inherit both into a Child class.

# Concept: Basic Multiple Inheritance.

# Requirements:

    # Father class should have a father_skill() method.
    # Mother class should have a mother_skill() method.
    # Child class should inherit both parent classes.
    # Child class should have its own child_skill() method.
    # Call all three methods using one Child object.

#----------------------------------------------------------------------------------------------------------------------------------

class Father:

    def father_skill(self):
        print('Father Skill: Driving')

class Mother:

    def monther_skill(self):
        print('Mother Skill: Cooking')

class child(Father,Mother):
    def child_specific(self):
        print('Child Skill: Programming')

c = child()
c.father_skill()
c.monther_skill()
c.child_specific()


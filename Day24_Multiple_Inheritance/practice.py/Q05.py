# Create two parent classes with constructors and inherit them into a Child class.

# Concept: Multiple Parent Constructors.

# Requirements:

    # Father constructor accepts father name.
    # Mother constructor accepts mother name.
    # Child constructor accepts both names and child name.
    # Initialize both parent attributes.
    # Display all names.

#---------------------------------------------------------------------------------------------------------



class Father:

    def __init__(self,father_name):
        self.father_name = father_name
        

class Mother:

    def __init__(self,mother_name):
        self.mother_name = mother_name 

class child(Father,Mother):

    def __init__(self, father_name , child_name):
        super().__init__(father_name)
        self.child_name = child_name


c= child('Rajesh','Rahul')
m = Mother('sunita')
print(f'Father = {c.father_name}')
print(f'Mother = {m.mother_name}')
print(f'Child  = {c.child_name}')
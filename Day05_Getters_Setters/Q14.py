# Create a Student class with:
    # _name
    # _maths
    # physics
    # _chemistry

# Requirements:
    # Subject marks must be between 0 and 100.
    # Use properties to access and update the marks.
    # Create a read-only total_marks property.
    # Create a read-only percentage property.

# Create three student objects and display their results.
#----------------------------------------------------------------------
class student:
    def __init__(self,name, maths,physics,chemistry):
        self._name = name
        self._maths = maths
        self._physics = physics
        self._chemistry = chemistry

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        self._name = new_name

    @property
    def maths(self):
        return self._maths
    @maths.setter
    def maths(self,new_maths):
        if 0 <= new_maths <= 100:
            self._maths = new_maths
        else:
            print('Marks must be 0 to 100')

    @property
    def physics(self):
        return self._physics
    @physics.setter
    def physics(self,new_physics):
        if 0 <= new_physics <= 100:
            self._physics = new_physics
        else:
            print('Marks must be 0 to 100')

    @property
    def chemistry(self):
        return self._chemistry
    @physics.setter
    def chemistry(self,new_chemistry):
        if 0 <= new_chemistry <= 100:
            self._chemistry = new_chemistry
        else:
            print('Marks must be 0 to 100')
    @property
    def total_marks(self):
        return self._maths + self._physics + self._chemistry
    @property
    def percentage(self):
        return self.total_marks   /3

    def info(self):
        print('Name =',self._name)
        print('Maths =',self._maths)
        print('Physics =',self._physics)
        print('Chemistry =',self._chemistry)
        print('Total Marks =',self.total_marks)
        print('Percenatge =',self.percentage,'%')
        print('----------------------------------------')

e1 = student('Sudhanshu',90,80,70)
e2 = student('kunal',80,70,60)
e3 = student('hitesh',50,40,80)

e1.maths = 95
e2.physics = 80
e3.chemistry = 90

e1.info()
e2.info()
e3.info()
# Create a Temperature class with a Celsius property and validation.

#-------------------------------------------------------------------------------------------

class Temperature:

    def __init__(self,Celsius ):
        self._Celsius  = Celsius 

    @property
    def Celsius(self):
        return self._Celsius 

    @Celsius.setter
    def Celsius(Self,new_Celsius):
        if new_Celsius < -273.15:
            raise ValueError('Temperature cannot be below absolute  zero')
        Self._Celsius = new_Celsius

temp  = Temperature(25)
print(temp.Celsius)

temp.celsius = 30
print(temp.celsius)

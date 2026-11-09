# Create a Transport parent class and a Bus child class.

# Concept: Inheritance with Calculation Logic.

# Requirements:

    # Parent stores distance.
    # Parent has a calculate_fare() method.
    # Child stores fare per kilometer.
    # Override the fare calculation method.
    # Calculate the total bus fare.

#-------------------------------------------------------------------------------------------------

class Transport:

    def __init__(self,distance):
        self.distance = distance

    def calculate_fare(self):
        return self.distance
    
class Bus(Transport):

    def __init__(self, distance,per_kilo):
        super().__init__(distance)
        self.per_kilo = per_kilo

    def calculate_fare(self):
        super().calculate_fare()
        print(f'Tota Bus Fare  = ₹{self.distance * self.per_kilo}')


s =Bus(50,12)
s.calculate_fare()
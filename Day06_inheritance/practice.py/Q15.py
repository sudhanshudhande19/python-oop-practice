# Create a parent class Transport with:
    # distance
    # calculate_fare()

# Create child classes:
    # Bus
    # Taxi
    # Train

# Fare rules:
    # Bus: ₹5 per kilometre
    # Taxi: ₹15 per kilometre
    # Train: ₹2 per kilometre

# Override calculate_fare() in each child class.
# Calculate the fare for a distance of 20 km and compare the results.

#----------------------------------------------------------------------------------------

class transport:
    def __init__(self,distance):
        self.distance = distance

    def calculate_fare(self):
        return 0
class bus(transport):
    def calculate_fare(self):
        return self.distance * 5

class taxi(transport):
    def calculate_fare(self):
        return self.distance * 15

class train(transport):
    def calculate_fare(self):
        return self.distance * 2

d1 = bus(100)
print('Bus Fare =₹',d1.calculate_fare())

d2 = taxi(100)
print('Taxi Fare =₹',d2.calculate_fare())

d3 = train(100)
print('Train Fare =₹',d3.calculate_fare())

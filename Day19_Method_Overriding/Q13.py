# Create a parent class Transport with a calculate_fare() method. Override it in Bus, Train, and Taxi.

#----------------------------------------------------------------------------------------------------------------------------------------


class Transport:
    def calculate_fare(self):
        print("Calculating transport fare")


class Bus(Transport):
    def calculate_fare(self):
        print("Bus Fare: ₹50")


class Train(Transport):
    def calculate_fare(self):
        print("Train Fare: ₹100")


class Taxi(Transport):
    def calculate_fare(self):
        print("Taxi Fare: ₹300")


b = Bus()
t = Train()
x = Taxi()

b.calculate_fare()
t.calculate_fare()
x.calculate_fare()
# Concept: Multilevel Inheritance with fare and capacity.

# Requirements:

    # Create Transport, Bus, and ElectricBus classes.
    # Transport stores vehicle name.
    # Bus stores passenger capacity.
    # ElectricBus stores battery capacity.
    # Create a method to calculate total fare.
    # Assume fare is ₹15 per passenger.
    # Display vehicle information and total fare for 20 passengers.

#_-----------------------------------------------------------------------------------------------------------------------------------------------------------

class Transport:
    def __init__(self, vehicle_name):
        self.vehicle_name = vehicle_name


class Bus(Transport):
    def __init__(self, vehicle_name, passenger_capacity):
        super().__init__(vehicle_name)
        self.passenger_capacity = passenger_capacity


class ElectricBus(Bus):
    def __init__(self, vehicle_name, passenger_capacity, battery_capacity):
        super().__init__(vehicle_name, passenger_capacity)
        self.battery_capacity = battery_capacity

    def calculate_total_fare(self, passengers):
        return passengers * 15

    def display_info(self):
        print("Vehicle Name:", self.vehicle_name)
        print("Passenger Capacity:", self.passenger_capacity)
        print("Battery Capacity:", self.battery_capacity, "kWh")



bus = ElectricBus("Tata Electric Bus", 50, 300)

bus.display_info()
print("Total Fare for 20 Passengers:", bus.calculate_total_fare(20))
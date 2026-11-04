# Create a Vehicle class with:
# vehicle_name
# vehicle_type
# price_per_day

# Create a method:
# calculate_rent(days)

# Rules:
# 1–3 days   → Normal price
# 4–7 days   → 10% discount
# 8+ days    → 20% discount

# Create at least 3 vehicles and calculate rental prices for different numbers of days.
#-----------------------------------------------------------------------------------------------------
class Vehicle:
    def __init__(self, vehicle_name, vehicle_type, price_per_day):
        self.vehicle_name = vehicle_name
        self.vehicle_type = vehicle_type
        self.price_per_day = price_per_day

    def calculate_rent(self, days):
        rent = self.price_per_day * days

        if 4 <= days <= 7:
            rent -= rent * 0.10  # 10% discount
        elif days >= 8:
            rent -= rent * 0.20  # 20% discount

        return rent

    def display(self, days):
        print(f"Vehicle Name : {self.vehicle_name}")
        print(f"Vehicle Type : {self.vehicle_type}")
        print(f"Price/Day    : ₹{self.price_per_day}")
        print(f"Days         : {days}")
        print(f"Total Rent   : ₹{self.calculate_rent(days)}")
        print("-" * 40)


# Create 3 vehicle objects
v1 = Vehicle("Honda City", "Car", 2000)
v2 = Vehicle("Royal Enfield", "Bike", 800)
v3 = Vehicle("Tata Ace", "Truck", 3000)

# Calculate rent for different days
v1.display(2)   # Normal Price
v2.display(5)   # 10% Discount
v3.display(10)  # 20% Discount
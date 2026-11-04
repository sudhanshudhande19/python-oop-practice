# Create a Mobile class with _battery.

# Rules:
    # Battery percentage must be between 0 and 100.
    # Invalid values should be rejected.
    # Use a property to read and update the battery percentage.
#---------------------------------------------------------------------
class Mobile:
    def __init__(self, battery):
        self._battery = 0
        self.battery = battery    # Uses setter

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self._battery = new_battery
            print("Battery Updated =", new_battery, "%")
        else:
            print("Invalid Battery Value Rejected")


obj = Mobile(60)
print("Current Battery =", obj.battery, "%")

obj.battery = 90
print("Current Battery =", obj.battery, "%")

obj.battery = 150
print("Current Battery =", obj.battery, "%")

obj.battery = -20
print("Current Battery =", obj.battery, "%")
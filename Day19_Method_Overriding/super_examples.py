"""
Day 19 - Method Overriding
super_examples.py - Extra examples of overriding with super()
"""


class Subscription:
    def __init__(self, user):
        self.user = user

    def monthly_fee(self):
        return 100

    def describe(self):
        print(f"{self.user}: base plan")


class FamilyPlan(Subscription):
    def __init__(self, user, members):
        super().__init__(user)               # parent sets user
        self.members = members               # child sets members

    def monthly_fee(self):
        return super().monthly_fee() + 50 * self.members     # reuse + extend

    def describe(self):
        super().describe()                   # parent line first
        print(f"  + {self.members} family members allowed")   # then the child's line


class Gadget:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f"{self.name} - Rs.{self.price}")


class Phone(Gadget):
    def __init__(self, name, price, camera_mp):
        super().__init__(name, price)
        self.camera_mp = camera_mp

    def show_info(self):
        super().show_info()
        print(f"  Camera: {self.camera_mp} MP")


class Laptop(Gadget):
    def show_info(self):                     # NO super(): completely replaced
        print(f"LAPTOP: {self.name}")


if __name__ == "__main__":
    print("--- Extend with super() ---")
    plan = FamilyPlan("Meera", 3)
    plan.describe()
    print("  fee:", plan.monthly_fee())

    print("\n--- super() in constructor and method ---")
    Phone("Pixel", 45000, 50).show_info()

    print("\n--- Replace without super() ---")
    Laptop("ThinkBook", 60000).show_info()

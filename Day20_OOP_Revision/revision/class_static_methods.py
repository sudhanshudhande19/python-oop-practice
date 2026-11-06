"""
Day 20 - OOP Revision
class_static_methods.py - Instance, class and static methods
"""


class Pizza:
    shop = "Pizza Point"                          # class variable
    total_made = 0

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings
        Pizza.total_made += 1

    # instance method -> needs an object (self)
    def describe(self):
        print(f"{self.size} pizza with {', '.join(self.toppings)}")

    # class method -> works with the class (cls); great for alternative constructors
    @classmethod
    def margherita(cls):
        return cls("medium", ["cheese", "tomato"])

    @classmethod
    def from_string(cls, data):                   # "large:cheese,corn"
        size, toppings = data.split(":")
        return cls(size.strip(), [t.strip() for t in toppings.split(",")])

    @classmethod
    def rename_shop(cls, new_name):
        cls.shop = new_name

    # static method -> no self, no cls; just a utility inside the class
    @staticmethod
    def is_valid_size(size):
        return size in ("small", "medium", "large")


if __name__ == "__main__":
    print("--- Instance method ---")
    p1 = Pizza("large", ["cheese", "olives"])
    p1.describe()

    print("\n--- Class methods as alternative constructors ---")
    Pizza.margherita().describe()
    Pizza.from_string("small: cheese, corn").describe()

    print("\n--- Class method changing class data ---")
    Pizza.rename_shop("Slice House")
    print("Shop:", Pizza.shop, "| Pizzas made:", Pizza.total_made)

    print("\n--- Static method (utility) ---")
    print("is_valid_size('large') :", Pizza.is_valid_size("large"))
    print("is_valid_size('huge')  :", Pizza.is_valid_size("huge"))

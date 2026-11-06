"""
Day 20 - OOP Revision
encapsulation.py - Public, protected, private, name mangling, property
"""


class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner                       # public
        self._currency = "INR"                   # protected (convention: don't touch)
        self.__balance = balance                 # private (name mangling)

    def get_balance(self):                       # getter method
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amount


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age                           # goes through the setter below

    @property                                    # getter
    def age(self):
        return self._age

    @age.setter                                  # setter with validation
    def age(self, value):
        if not 0 <= value <= 120:
            raise ValueError("Age must be between 0 and 120")
        self._age = value


if __name__ == "__main__":
    print("--- Private attribute ---")
    w = Wallet("Rahul", 1000)
    w.deposit(500)
    print("Balance:", w.get_balance())
    try:
        print(w.__balance)
    except AttributeError as error:
        print("Error:", error)

    print("\n--- Name mangling: the real stored name ---")
    print(w.__dict__)
    print("w._Wallet__balance =", w._Wallet__balance, "(possible, but never do this)")

    print("\n--- Validation inside methods ---")
    for action, amount in [("deposit", -5), ("withdraw", 99999)]:
        try:
            getattr(w, action)(amount)
        except ValueError as error:
            print(f"{action}({amount}) ->", error)

    print("\n--- Property (getter + setter) ---")
    p = Person("Amit", 25)
    print("age:", p.age)
    p.age = 30                                   # looks like an attribute, runs the setter
    print("age:", p.age)
    try:
        p.age = -4
    except ValueError as error:
        print("Error:", error)

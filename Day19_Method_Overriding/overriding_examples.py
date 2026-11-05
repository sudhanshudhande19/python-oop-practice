"""
Day 19 - Method Overriding
overriding_examples.py - Extra examples of overriding and runtime polymorphism
"""


class Instrument:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f"{self.name}: making a sound")

    def tune(self):
        print(f"{self.name}: tuned")


class Guitar(Instrument):
    def play(self):                          # overrides play()
        print(f"{self.name}: strumming the strings")


class Drum(Instrument):
    def play(self):                          # overrides play()
        print(f"{self.name}: hitting the skin")


class Flute(Instrument):
    pass                                     # overrides nothing -> uses parent's play()


class Subscription:
    def __init__(self, user):
        self.user = user

    def monthly_fee(self):
        return 100

    def describe(self):
        print(f"{self.user}: base plan")


class StudentPlan(Subscription):
    def monthly_fee(self):                   # REPLACES the parent's value
        return 50


if __name__ == "__main__":
    print("--- Runtime polymorphism ---")
    band = [Guitar("Guitar"), Drum("Drum"), Flute("Flute"), Instrument("Generic")]
    for instrument in band:
        instrument.play()                    # same call, different behaviour
        instrument.tune()                    # inherited by all

    print("\n--- Replacing a value ---")
    for plan in [Subscription("Ann"), StudentPlan("Raj")]:
        plan.describe()
        print("  fee:", plan.monthly_fee())

    print("\n--- isinstance() check ---")
    g = Guitar("Guitar")
    print("Guitar is an Instrument:", isinstance(g, Instrument))
    print("Guitar is a Drum       :", isinstance(g, Drum))

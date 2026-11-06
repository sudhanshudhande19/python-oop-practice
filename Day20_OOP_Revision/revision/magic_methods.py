"""
Day 20 - OOP Revision
magic_methods.py - __init__, __str__, __repr__, __add__, __eq__, __lt__, __len__, __contains__
"""


class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Rs.{self.amount}"

    def __repr__(self):
        return f"Money({self.amount!r})"

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)      # new object, originals unchanged

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount

    def __lt__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount < other.amount


class Basket:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items


if __name__ == "__main__":
    a = Money(100)
    b = Money(250)

    print("--- __str__ and __repr__ ---")
    print(a)
    print(repr(a))
    print([a, b])

    print("\n--- __add__ ---")
    print(a + b)
    print("originals:", a, b)

    print("\n--- __eq__ and __lt__ ---")
    print("a == b:", a == b)
    print("a == Money(100):", a == Money(100))
    print("a < b :", a < b)
    print("sorted:", sorted([b, a]))

    print("\n--- __len__ and __contains__ ---")
    basket = Basket(["apple", "milk", "bread"])
    print("len(basket)        :", len(basket))
    print("'milk' in basket   :", "milk" in basket)
    print("'tea' in basket    :", "tea" in basket)
    print("bool(Basket([]))   :", bool(Basket([])))

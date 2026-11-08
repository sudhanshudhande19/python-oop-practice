"""
Day 22 - Python OOP: Operator Overloading
theory/magic_methods.py - Theory examples

Run this file and, for every line, say WHICH magic method Python calls.
"""

from functools import total_ordering


def heading(title):
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


# ---------------------------------------------------------
# 1. Operators already behave differently for different types
# ---------------------------------------------------------
heading("1. Built-in operator overloading")

print(10 + 20)               # numbers  -> addition
print("Hello " + "Python")   # strings  -> joining
print([1, 2] + [3])          # lists    -> joining
print([0] * 3)               # list * int -> repetition


# ---------------------------------------------------------
# 2. Overloading + (returns a plain number, as in the notes)
# ---------------------------------------------------------
heading("2. __add__ returning a number")


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):          # n1 + n2  ->  n1.__add__(n2)
        return self.value + other.value


n1 = Number(10)
n2 = Number(20)
print(n1 + n2)


# ---------------------------------------------------------
# 3. Overloading > (comparison)
# ---------------------------------------------------------
heading("3. __gt__")


class Student:
    def __init__(self, marks):
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks


s1 = Student(85)
s2 = Student(70)
print(s1 > s2)
print(s2 > s1)


# ---------------------------------------------------------
# 4. All arithmetic operators - returning NEW objects
# ---------------------------------------------------------
heading("4. +  -  *  /  //  %  **  (returning new objects)")


class Value:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Value(self.number + other.number)

    def __sub__(self, other):
        return Value(self.number - other.number)

    def __mul__(self, other):
        return Value(self.number * other.number)

    def __truediv__(self, other):
        return Value(self.number / other.number)

    def __floordiv__(self, other):
        return Value(self.number // other.number)

    def __mod__(self, other):
        return Value(self.number % other.number)

    def __pow__(self, other):
        return Value(self.number ** other.number)

    def __repr__(self):
        return f"Value({self.number})"


a = Value(17)
b = Value(5)
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)
print("originals unchanged:", a, b)


# ---------------------------------------------------------
# 5. NotImplemented
# ---------------------------------------------------------
heading("5. NotImplemented (unsupported types)")


class Weight:
    def __init__(self, grams):
        if grams < 0:
            raise ValueError("Weight cannot be negative")
        self.grams = grams

    def __str__(self):
        kg, g = divmod(self.grams, 1000)
        return f"{kg} kg {g} g"

    def __repr__(self):
        return f"Weight({self.grams!r})"

    def __add__(self, other):
        if not isinstance(other, Weight):
            return NotImplemented          # NOTE: return, not raise!
        return Weight(self.grams + other.grams)

    def __sub__(self, other):
        if not isinstance(other, Weight):
            return NotImplemented
        return Weight(self.grams - other.grams)

    def __mul__(self, factor):             # Weight * number
        if not isinstance(factor, (int, float)):
            return NotImplemented
        return Weight(round(self.grams * factor))

    __rmul__ = __mul__                     # number * Weight

    def __truediv__(self, other):
        if isinstance(other, Weight):      # Weight / Weight -> plain ratio
            if other.grams == 0:
                raise ZeroDivisionError("Cannot divide by a zero weight")
            return self.grams / other.grams
        if isinstance(other, (int, float)):  # Weight / number -> Weight
            return Weight(round(self.grams / other))
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Weight):
            return NotImplemented
        return self.grams == other.grams

    def __lt__(self, other):
        if not isinstance(other, Weight):
            return NotImplemented
        return self.grams < other.grams


w1 = Weight(1500)
w2 = Weight(750)
print("w1 + w2       :", w1 + w2)
print("w1 - w2       :", w1 - w2)
print("w1 * 2        :", w1 * 2)
print("2 * w1        :", 2 * w1, "(works because of __rmul__)")
print("w1 / 2        :", w1 / 2)
print("w1 / w2       :", w1 / w2)

try:
    w1 + 5
except TypeError as error:
    print("w1 + 5        -> TypeError:", error)

try:
    w2 - w1
except ValueError as error:
    print("w2 - w1       -> ValueError:", error)


# ---------------------------------------------------------
# 6. Comparison operators
# ---------------------------------------------------------
heading("6. Comparison operators")

print("w1 == Weight(1500):", w1 == Weight(1500))
print("w1 != w2          :", w1 != w2, "(free from __eq__)")
print("w2 < w1           :", w2 < w1)
print("w1 > w2           :", w1 > w2, "(Python uses w2.__lt__(w1))")
print("sorted            :", sorted([w1, w2]))
print("max               :", max(w1, w2))

try:
    w1 <= w2
except TypeError as error:
    print("w1 <= w2          -> TypeError:", error)

try:
    {w1}
except TypeError as error:
    print("set of Weight     -> TypeError:", error)


# ---------------------------------------------------------
# 7. total_ordering writes the other comparisons for you
# ---------------------------------------------------------
heading("7. functools.total_ordering")


@total_ordering
class Version:
    def __init__(self, text):
        self.text = text
        self.parts = tuple(int(part) for part in text.split("."))

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts == other.parts

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts < other.parts

    def __repr__(self):
        return f"Version('{self.text}')"


v1 = Version("1.9")
v2 = Version("1.10.2")
print("v1 < v2  :", v1 < v2)
print("v1 <= v2 :", v1 <= v2)
print("v1 >= v2 :", v1 >= v2)
print("max      :", max(v1, v2))


# ---------------------------------------------------------
# 8. sum() starts with 0, so give it a start value
# ---------------------------------------------------------
heading("8. sum() with custom objects")

try:
    sum([w1, w2])
except TypeError as error:
    print("sum([w1, w2])            -> TypeError:", error)

print("sum([w1, w2], Weight(0)) :", sum([w1, w2], Weight(0)))


# ---------------------------------------------------------
# 9. Container operators: len(), in, []
# ---------------------------------------------------------
heading("9. __len__, __contains__, __getitem__")


class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)

    def __add__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented
        return Playlist(self.songs + other.songs)      # new list -> originals unchanged

    def __len__(self):
        return len(self.songs)

    def __contains__(self, song):
        return song in self.songs

    def __getitem__(self, index):
        return self.songs[index]

    def __repr__(self):
        return f"Playlist({self.songs!r})"


p1 = Playlist(["Faded", "Believer"])
p2 = Playlist(["Closer"])
combined = p1 + p2
print("combined      :", combined)
print("len(combined) :", len(combined))
print("'Faded' in    :", "Faded" in combined)
print("'Hello' in    :", "Hello" in combined)
print("combined[0]   :", combined[0])
print("combined[-1]  :", combined[-1])
print("combined[0:2] :", combined[0:2])
print("for loop      :", [song for song in combined], "(works because of __getitem__)")
print("originals     :", p1, p2)

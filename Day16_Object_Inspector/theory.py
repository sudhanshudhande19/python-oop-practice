"""
Day 16 - Python OOP: dir(), __dict__ and help()
theory.py - Examples of dir(), __dict__ and help()

Run this file and read the output carefully.
Try to predict the output of each example BEFORE you run it.
"""


def heading(title):
    print("\n" + "=" * 55)
    print(title)
    print("=" * 55)


def public_names(obj):
    """Return only the names that do NOT start with double underscores."""
    return [name for name in dir(obj) if not name.startswith("__")]


class Student:
    """Represents a student with a name and marks."""

    school = "ABC School"          # class attribute (shared by all objects)

    def __init__(self, name, marks):
        self.name = name           # instance attribute
        self.marks = marks         # instance attribute

    def study(self):
        """Print a study message."""
        print(f"{self.name} is studying")


s1 = Student("Rahul", 85)


# ---------------------------------------------------------
# 1. type() - What are you?
# ---------------------------------------------------------
heading("1. type() - What kind of object is it?")

print(type(s1))
print(type(5))
print(type("hello"))
print("Class name:", type(s1).__name__)


# ---------------------------------------------------------
# 2. dir() - What is available?
# ---------------------------------------------------------
heading("2. dir() - What names are available?")

print("Full dir(s1) (long, includes special methods):")
print(dir(s1))

print("\nOnly our own names (filtered):")
print(public_names(s1))

print("\nSome built-in types:")
print("str  :", public_names("hello")[:6], "...")
print("list :", public_names([1, 2, 3])[:6], "...")
print("dict :", public_names({"a": 1})[:6], "...")


# ---------------------------------------------------------
# 3. Attribute vs method
# ---------------------------------------------------------
heading("3. Attribute or method? (using callable)")

for name in public_names(s1):
    kind = "method" if callable(getattr(s1, name)) else "attribute"
    print(f"{name:<8} -> {kind}")


# ---------------------------------------------------------
# 4. Magic (special) methods
# ---------------------------------------------------------
heading("4. Special (magic) methods")

for special in ["__init__", "__str__", "__class__", "__dict__"]:
    print(f"{special:<10} in dir(s1): {special in dir(s1)}")


# ---------------------------------------------------------
# 5. __dict__ - What data is stored?
# ---------------------------------------------------------
heading("5. __dict__ - Stored attributes")

print("s1.__dict__ :", s1.__dict__)
print("vars(s1)    :", vars(s1))


# ---------------------------------------------------------
# 6. dir() vs __dict__
# ---------------------------------------------------------
heading("6. dir() vs __dict__")

print("'study' in dir(s1)       :", "study" in dir(s1))
print("'study' in s1.__dict__   :", "study" in s1.__dict__)
print("'name'  in s1.__dict__   :", "name" in s1.__dict__)
print("'school' in s1.__dict__  :", "school" in s1.__dict__)
print("'school' in Student.__dict__:", "school" in Student.__dict__)

print("\nOwn names stored in the CLASS:")
print([key for key in Student.__dict__ if not key.startswith("__")])


# ---------------------------------------------------------
# 7. Changing data and adding attributes dynamically
# ---------------------------------------------------------
heading("7. Update data and add new attributes")

print("Before :", s1.__dict__)
s1.marks = 90                      # update an existing value
s1.grade = "A"                     # add a NEW attribute
s1.__dict__["city"] = "Pune"       # add through the dictionary
print("After  :", s1.__dict__)
print("s1.grade =", s1.grade, "| s1.city =", s1.city)


# ---------------------------------------------------------
# 8. Comparing two objects
# ---------------------------------------------------------
heading("8. Comparing two objects with __dict__")

a = Student("Rahul", 85)
b = Student("Amit", 85)
print("a:", a.__dict__)
print("b:", b.__dict__)

for key in a.__dict__:
    status = "same" if a.__dict__[key] == b.__dict__[key] else "DIFFERENT"
    print(f"{key:<6} -> {status}")


# ---------------------------------------------------------
# 9. Not every object has __dict__
# ---------------------------------------------------------
heading("9. Objects without __dict__")


class Point:
    __slots__ = ("x", "y")         # no __dict__ for this class

    def __init__(self, x, y):
        self.x = x
        self.y = y


for item in [s1, 5, "hi", [1, 2], Point(3, 4)]:
    print(f"{type(item).__name__:<8} has __dict__: {hasattr(item, '__dict__')}")

try:
    print((5).__dict__)
except AttributeError as error:
    print("Error:", error)


# ---------------------------------------------------------
# 10. help() - How does it work?
# ---------------------------------------------------------
heading("10. help() and docstrings")

print("Docstring of the class  :", Student.__doc__)
print("Docstring of the method :", Student.study.__doc__)

print("\n--- help(str.upper) ---")
help(str.upper)

print("\n--- help(Student) ---")
help(Student)


# ---------------------------------------------------------
# 11. Comparing two types (Bonus technique)
# ---------------------------------------------------------
heading("11. Methods only a list has (not a tuple)")

only_in_list = set(dir(list)) - set(dir(tuple))
print(sorted(name for name in only_in_list if not name.startswith("__")))
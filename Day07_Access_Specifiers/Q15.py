# Create a class Demo with:

    # A public attribute name
    # A protected-by-convention attribute _age
    # A private attribute __salary

# Create an object and try to access all three attributes.
# Observe the results.
# Then, research what name mangling does to __salary and explain why accessing a mangled name is not the recommended way to design a class's public interface.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Demo:
    def __init__(self, name, age, salary):
        self.name = name
        self._age = age
        self.__salary = salary


d1 = Demo("Sudhanshu", 22, 50000)

# Access all three attributes
print("Name:", d1.name)
print("Age:", d1._age)

# This will raise an AttributeError
try:
    print("Salary:", d1.__salary)
except AttributeError:
    print("Cannot access __salary directly")

# Name-mangled access (for demonstration only)
print("Salary using mangled name:", d1._Demo__salary)

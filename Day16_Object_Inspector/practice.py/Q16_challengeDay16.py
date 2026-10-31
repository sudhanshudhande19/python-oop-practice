
class ObjectInspector:

    def __init__(self, target_object, object_name):
        self.target_object = target_object
        self.object_name = object_name

    # 1. Show available attributes and methods
    def show_attributes(self):
        print("\nAvailable Attributes and Methods")

        attributes = dir(self.target_object)

        for attribute in attributes:
            print(attribute)

    # 2. Show stored object data
    def show_object_data(self):
        print("\nObject Stored Data")

        if hasattr(self.target_object, "__dict__"):
            print(self.target_object.__dict__)
        else:
            print("This object does not have a __dict__ attribute.")

    # 3. Show documentation
    def show_documentation(self):
        print("\nObject Documentation")

        help(self.target_object)

    # 4. Show class name
    def show_class_name(self):
        print("\nObject Class Name")

        print(type(self.target_object).__name__)

    # 5. Complete inspection
    def inspect_object(self):
        print("\n" + "=" * 40)
        print(f"INSPECTING: {self.object_name}")
        print("=" * 40)

        self.show_class_name()
        self.show_object_data()
        self.show_attributes()

        print("\nDocumentation:")
        self.show_documentation()


# ==================================
# TEST OBJECT 1: CUSTOM CLASS OBJECT
# ==================================

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)


s1 = Student("Sudhanshu", 85)

inspector1 = ObjectInspector(s1, "Student Object")
inspector1.inspect_object()


# ==================================
# TEST OBJECT 2: LIST OBJECT
# ==================================

my_list = [10, 20, 30, 40]

inspector2 = ObjectInspector(my_list, "List Object")
inspector2.inspect_object()


# ==================================
# TEST OBJECT 3: INTEGER OBJECT
# ==================================

my_number = 100

inspector3 = ObjectInspector(my_number, "Integer Object")
inspector3.inspect_object()

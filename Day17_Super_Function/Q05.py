# Create a Shape class with a method display().

# Create a Rectangle class that overrides display().

# Call the parent method using super().

#---------------------------------------------------------------------------------------------------------
class Shape:
    def display(self):
        print("This is a Shape.")


class Rectangle(Shape):
    def display(self):
        super().display()  
        print("This is a Rectangle.")



rect = Rectangle()
rect.display()
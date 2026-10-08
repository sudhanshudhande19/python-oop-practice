# reate a Circle class with:(radius) Create two methods: area() ,circumference()
# Use:
# Area = π × r²
# Circumference = 2 × π × r
#--------------------------------------------------------------------
class Circle:
    radius = 5
    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius
        
    def info(self):
        print(f"Area = {self.area()}\nCircumference = {self.circumference()}")

obj = Circle()
obj.area()
obj.circumference()
obj.info()
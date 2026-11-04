# Create a Circle class with:
# radius

# Create a method:
# area()

# Create three circle objects.
# Find and display:
# Area of each circle
# Circle with the largest area
# Circle with the smallest area
#--------------------------------------------------------
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Create three circle objects
c1 = Circle(5)
c2 = Circle(8)
c3 = Circle(3)

circles = [c1, c2, c3]

# Area of each circle
print("Area of Each Circle:")
for i, circle in enumerate(circles, start=1):
    print(f"Circle {i} (Radius = {circle.radius}) : {circle.area():.2f}")

# Circle with largest area
largest = max(circles, key=lambda c: c.area())
print(f"\nLargest Area Circle:")
print(f"Radius = {largest.radius}, Area = {largest.area():.2f}")

# Circle with smallest area
smallest = min(circles, key=lambda c: c.area())
print(f"\nSmallest Area Circle:")
print(f"Radius = {smallest.radius}, Area = {smallest.area():.2f}")
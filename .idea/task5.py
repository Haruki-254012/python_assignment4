import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius**2, 1)

rect = Rectangle(4, 5)
circ = Circle(5)
print(f"Rectangle area: {rect.area()}")
print(f"Circle area: {circ.area()}")

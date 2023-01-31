class Shape:
    def __init__(self, color):
        self.color = color
    
class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(10, 5, "Red")
print("Rectangle area:", r.area())
print("Rectangle color:", r.color)

c = Circle(5, "Green")
print("Circle area:", c.area())
print("Circle color:", c.color)

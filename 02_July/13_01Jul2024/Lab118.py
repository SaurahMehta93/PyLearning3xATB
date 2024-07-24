# Polymorphism
# method overriding

class Shape:
    def area(self):
        return "Area of a shape"

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(2, 3)
print(shape1.area())

shape2 = Circle(10)
print(shape2.area())

shape3 = Shape()
print(shape3.area())
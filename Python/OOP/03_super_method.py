import math

class Shapes():
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'} ")
        
class Circle(Shapes):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
    
    # method overriding
    def describe(self):
        print(f"The circle has an area of {math.pi * self.radius ** 2:.2f}cm^2")
        super().describe()
         
class Square(Shapes):
    def __init__(self, color, filled, length):
        super().__init__(color, filled)
        self.length = length
    
    def describe(self):
            print(f"The square has an area of {self.length ** 2}cm^2")
            super().describe()
        
class Triangle(Shapes):
    def __init__(self, color, filled, length, height):
        super().__init__(color, filled)
        self.length = length
        self.height = height
        
    def describe(self):
            print(f"The Triangle has an area of {(1/2) * self.length * self.height}cm^2")
            super().describe()
        
circle = Circle("Red", True, 5)
circle.describe()
print()
square = Square("Blue", False, 8)
square.describe()
print()
triangle = Triangle("Blue", False, 3, 4)
triangle.describe()
print()


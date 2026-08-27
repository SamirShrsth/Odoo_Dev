# Polymorphism Concept
# Similar to interfaces in java
from abc import ABC, abstractmethod
import math

class Shape():
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"Area of Circle: {math.pi * self.radius ** 2:.2f}")
        
class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        print(f"Area of Square: {self.length ** 2:.2f}cm^2")
        
class Triangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height
    
    def area(self):
        print(f"Area of Triangle: {(1/2) * self.length * self.height}cm^2")
    
circle: Circle = Circle(5)
circle.area()
square: Square = Square(5)
square.area()
triangle: Triangle = Triangle(5, 6)
triangle.area()
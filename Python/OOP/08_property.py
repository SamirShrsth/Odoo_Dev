# @property = access to getters, setters and deletetors

class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height
     
    @property   
    def width(self):
        return f"{self._width:.2f}cm"
    
    @property 
    def height(self):
        return f"{self._height:.2f}cm"
    
rectangle1 = Rectangle(3,4)
print(rectangle1.width)
print(rectangle1.height)


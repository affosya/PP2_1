class Shape:
    def area(self):
        return 0  # Default area for shape is 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  # Set length of rectangle
        self.width = width  # Set width of rectangle

    def area(self):
        return self.length * self.width  # Calculate area of rectangle

# Example Usage
rectangle = Rectangle(4, 5)  # Create a rectangle with length 4 and width 5
print("Area of the rectangle:", rectangle.area())  # Output area

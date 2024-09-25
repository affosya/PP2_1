class Shape:
    def area(self):
        return 0  # Default area for shape is 0

class Square(Shape):
    def __init__(self, length):
        self.length = length  # Set the length of the square

    def area(self):
        return self.length ** 2  # Calculate area of square

# Example Usage
square = Square(4)  # Create a square with side length 4
print("Area of the square:", square.area())  # Output area

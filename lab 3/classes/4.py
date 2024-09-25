import math  # For distance calculation

class Point:
    def __init__(self, x, y):
        self.x = x  # Set x coordinate
        self.y = y  # Set y coordinate

    def show(self):
        print("Point coordinates: (", self.x, ",", self.y, ")")  # Display coordinates

    def move(self, dx, dy):
        self.x += dx  # Change x coordinate
        self.y += dy  # Change y coordinate

    def dist(self, other):
        # Calculate distance to another point
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Example Usage
point1 = Point(1, 2)  # Create first point
point2 = Point(4, 6)  # Create second point
point1.show()  # Show coordinates of first point
point2.show()  # Show coordinates of second point
print("Distance between points:", point1.dist(point2))  # Output distance

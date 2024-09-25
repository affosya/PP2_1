import math

def sphere_volume(radius):
    # Volume formula for a sphere: V = (4/3) * π * r^3
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Example usage:
radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")

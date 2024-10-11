import math

def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

# Example usage
radius = 5
circle_area = calculate_circle_area(radius)
print(f"The area of a circle with radius {radius} is: {circle_area:.2f}")

side = 4
square_area = calculate_square_area(side)
print(f"The area of a square with side length {side} is: {square_area}")

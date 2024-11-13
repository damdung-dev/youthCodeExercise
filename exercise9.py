import math

def angle_quadrant(x):
    # Convert minutes to degrees
    degrees = x / 60
    radians = math.radians(degrees)
    quadrant = (degrees % 360) // 90 + 1
    cosine_value = math.cos(radians)
    return quadrant, cosine_value

# Example usage
x = float(input("Enter angle in minutes: "))
quadrant, cosine_value = angle_quadrant(x)
print(f"The angle is in quadrant {int(quadrant)}")
print("cos(x) =", cosine_value)

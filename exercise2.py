import math

def distance(xA, yA, xB, yB):
    return math.sqrt((xB - xA)**2 + (yB - yA)**2)

# Example usage
xA, yA = map(float, input("Enter coordinates of point A (xA, yA): ").split())
xB, yB = map(float, input("Enter coordinates of point B (xB, yB): ").split())
print("The distance AB is:", distance(xA, yA, xB, yB))

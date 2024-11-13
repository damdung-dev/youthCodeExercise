def point_in_circle(xC, yC, R, xM, yM):
    distance = math.sqrt((xM - xC)**2 + (yM - yC)**2)
    if distance < R:
        return "inside"
    elif distance == R:
        return "on"
    else:
        return "outside"

# Example usage
xC, yC = map(float, input("Enter center coordinates (xC, yC): ").split())
R = float(input("Enter radius R: "))
xM, yM = map(float, input("Enter point coordinates (xM, yM): ").split())
print("Point M is", point_in_circle(xC, yC, R, xM, yM), "the circle.")

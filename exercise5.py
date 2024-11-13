def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def point_in_triangle(xA, yA, xB, yB, xC, yC, xM, yM):
    # Calculate area of triangle ABC
    area_ABC = area(xA, yA, xB, yB, xC, yC)
    
    # Calculate area of triangles AMB, BMC, and CAM
    area_AMB = area(xA, yA, xM, yM, xB, yB)
    area_BMC = area(xB, yB, xM, yM, xC, yC)
    area_CAM = area(xC, yC, xM, yM, xA, yA)
    
    # Check if the sum of AMB, BMC and CAM equals ABC
    if area_ABC == area_AMB + area_BMC + area_CAM:
        if area_AMB == 0 or area_BMC == 0 or area_CAM == 0:
            return "on"
        return "inside"
    else:
        return "outside"

# Example usage
xA, yA = map(float, input("Enter coordinates of point A (xA, yA): ").split())
xB, yB = map(float, input("Enter coordinates of point B (xB, yB): ").split())
xC, yC = map(float, input("Enter coordinates of point C (xC, yC): ").split())
xM, yM = map(float, input("Enter coordinates of point M (xM, yM): ").split())
print("Point M is", point_in_triangle(xA, yA, xB, yB, xC, yC, xM, yM), "the triangle ABC.")

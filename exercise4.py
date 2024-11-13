import math

def triangle_type_and_area(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        # Determine type of triangle
        if a == b == c:
            triangle_type = "Equilateral"
        elif a == b or b == c or a == c:
            triangle_type = "Isosceles"
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            triangle_type = "Right"
        else:
            triangle_type = "Scalene"
        
        return triangle_type, area
    else:
        return "Invalid triangle", None

# Example usage
a, b, c = map(float, input("Enter the three sides of the triangle: ").split())
triangle_type, area = triangle_type_and_area(a, b, c)
if area:
    print("Triangle type:", triangle_type)
    print("Area:", area)
else:
    print(triangle_type)

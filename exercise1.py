import math

def sphere_volume(S):
    R = math.sqrt(S / (4 * math.pi))
    V = (4/3) * math.pi * R**3
    return V

# Example usage
S = float(input("Enter the surface area S of the sphere: "))
print("The volume V is:", sphere_volume(S))

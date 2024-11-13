import math

def gcd_lcm(a, b):
    gcd_value = math.gcd(a, b)
    lcm_value = abs(a * b) // gcd_value
    return gcd_value, lcm_value

# Example usage
a, b = map(int, input("Enter two positive integers a and b: ").split())
gcd_value, lcm_value = gcd_lcm(a, b)
print("GCD:", gcd_value)
print("LCM:", lcm_value)

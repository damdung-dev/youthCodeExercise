import numpy as np
from math import gcd

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

a, b = map(int, input("Nhập hai số nguyên dương a, b: ").split())
gcd_value = gcd(a, b)
lcm_value = lcm(a, b)
print(f"Ước số chung lớn nhất của {a} và {b}: {gcd_value}")
print(f"Bội số chung nhỏ nhất của {a} và {b}: {lcm_value}")

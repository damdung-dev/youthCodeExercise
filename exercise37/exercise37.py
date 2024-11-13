import numpy as np

def find_largest_m(n):
    total = 0
    m = 0
    while total + (m + 1) < n:
        m += 1
        total += m
    return m, total

n = int(input("Nhập n: "))
m, total_sum = find_largest_m(n)
print(f"1 + 2 + ... + {m} = {total_sum} < {n}")
print(f"m = {m}")

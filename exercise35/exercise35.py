import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_prime_below(n):
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i
    return None

n = int(input("Nhập n: "))
if is_prime(n):
    print(f"{n} là số nguyên tố")
else:
    largest_prime = find_largest_prime_below(n)
    print(f"{n} không phải là số nguyên tố")
    print(f"Số nguyên tố bé hơn gần nhất: {largest_prime}")

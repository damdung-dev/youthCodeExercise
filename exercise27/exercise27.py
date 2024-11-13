import numpy as np

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

n = int(input("Nhập n: "))
factors = prime_factors(n)
print(f"Các thừa số nguyên tố của {n}: {' * '.join(map(str, factors))}")

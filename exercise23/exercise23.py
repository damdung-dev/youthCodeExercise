import numpy as np

def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def find_perfect_numbers(limit):
    perfect_numbers = [n for n in range(2, limit) if is_perfect(n)]
    return perfect_numbers

n = int(input("Nhập n: "))
perfect_numbers = find_perfect_numbers(n)
print(f"Các số hoàn hảo nhỏ hơn {n}: {perfect_numbers}")

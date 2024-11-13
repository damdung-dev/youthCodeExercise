import numpy as np

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return sum([d ** num_digits for d in digits]) == n

def find_armstrong_numbers():
    armstrong_numbers = []
    for n in range(100, 10000):
        if is_armstrong(n):
            armstrong_numbers.append(n)
    return armstrong_numbers

print("Các số Armstrong có 3 hoặc 4 chữ số: ", find_armstrong_numbers())

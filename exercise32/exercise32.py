import numpy as np

def hailstone_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

n = int(input("Nhập n: "))
sequence = hailstone_sequence(n)
print(f"Chuỗi hailstone: {sequence}")
print(f"Số lượng số trong chuỗi: {len(sequence)}")

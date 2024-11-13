import numpy as np
from math import gcd

def check_coprime_pairs(arr):
    coprime_pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if gcd(arr[i], arr[j]) == 1:
                coprime_pairs.append((arr[i], arr[j]))
    return coprime_pairs

def sum_even_odd_positions(arr):
    even_sum = sum(arr[i] for i in range(1, len(arr), 2))
    odd_sum = sum(arr[i] for i in range(0, len(arr), 2))
    return even_sum, odd_sum

def generate_random_array(n):
    return np.random.randint(10, 21, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_random_array(n)
print(f"Mảng đã tạo: {arr}")

even_sum, odd_sum = sum_even_odd_positions(arr)
print(f"Tổng các số chẵn ở vị trí lẻ: {even_sum}")
print(f"Tổng các số lẻ ở vị trí chẵn: {odd_sum}")

coprime_pairs = check_coprime_pairs(arr)
if coprime_pairs:
    print(f"Các cặp nguyên tố cùng nhau: {coprime_pairs}")
else:
    print("Không có cặp nguyên tố cùng nhau nào trong mảng.")

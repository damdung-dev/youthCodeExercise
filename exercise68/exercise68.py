import numpy as np

def divide_array_min_difference(arr):
    arr_sorted = sorted(arr, reverse=True)
    group1, group2 = [], []
    for num in arr_sorted:
        if sum(group1) <= sum(group2):
            group1.append(num)
        else:
            group2.append(num)
    return group1, group2

def generate_array(n):
    return np.random.randint(100, 201, size=n)

n = int(input("Nhập số phần tử của mảng (chẵn): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

group1, group2 = divide_array_min_difference(arr)
print(f"Nhóm 1: {group1} với tổng {sum(group1)}")
print(f"Nhóm 2: {group2} với tổng {sum(group2)}")
print(f"Hiệu nhỏ nhất giữa hai tổng: {abs(sum(group1) - sum(group2))}")

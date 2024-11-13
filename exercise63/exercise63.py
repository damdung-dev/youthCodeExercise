import numpy as np

def count_divisible_by_4_ending_with_6(arr):
    count = 0
    for num in arr:
        if num % 4 == 0 and str(num)[-1] == '6':
            count += 1
    return count

def double_odd_elements(arr):
    return [x * 2 if x % 2 != 0 else x for x in arr]

def generate_random_array(n):
    return np.random.randint(-100, 101, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_random_array(n)
print(f"Mảng đã tạo: {arr}")

count = count_divisible_by_4_ending_with_6(arr)
print(f"Có {count} phần tử chia hết cho 4 và có chữ số cuối là 6")

modified_arr = double_odd_elements(arr)
print(f"Mảng sau khi nhân đôi các phần tử lẻ: {modified_arr}")

import numpy as np

def sum_positive_integers(arr):
    return np.sum(arr[arr > 0])

def delete_element(arr, index):
    return np.delete(arr, index)

def generate_random_array(n):
    return np.random.randint(-100, 101, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_random_array(n)
print(f"Mảng đã tạo: {arr}")

sum_positive = sum_positive_integers(arr)
print(f"Tổng các số nguyên dương trong mảng: {sum_positive}")

p = int(input(f"Nhập chỉ số phần tử muốn xóa (0 đến {n-1}): "))
arr_after_deletion = delete_element(arr, p)
print(f"Mảng sau khi xóa phần tử: {arr_after_deletion}")

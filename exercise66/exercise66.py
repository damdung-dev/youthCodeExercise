import numpy as np

def find_min_max(arr):
    return min(arr), max(arr)

def remove_all_but_first_max(arr, max_value):
    first_max_index = arr.index(max_value)
    return [arr[i] for i in range(len(arr)) if i == first_max_index or arr[i] != max_value]

def generate_array(n):
    return np.random.randint(-100, 101, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

min_value, max_value = find_min_max(arr)
print(f"Giá trị nhỏ nhất: {min_value}")
print(f"Giá trị lớn nhất: {max_value}")

arr_after_removal = remove_all_but_first_max(arr, max_value)
print(f"Mảng sau khi xóa tất cả các phần tử lớn nhất trừ phần tử đầu tiên: {arr_after_removal}")

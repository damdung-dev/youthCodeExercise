import numpy as np

def is_power_of_2(n):
    return (n > 0) and (n & (n - 1)) == 0

def count_powers_of_2(arr):
    return sum(1 for x in arr if is_power_of_2(x))

def remove_elements(arr, x):
    return [element for element in arr if element != x]

def generate_array(n):
    return np.random.randint(1, 100, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

powers_of_2_count = count_powers_of_2(arr)
print(f"Có {powers_of_2_count} phần tử là lũy thừa của 2")

x = int(input("Nhập x để xóa các phần tử có giá trị bằng x: "))
arr_after_removal = remove_elements(arr, x)
print(f"Mảng sau khi xóa các phần tử bằng {x}: {arr_after_removal}")

import numpy as np

def sort_even_odd_separately(arr):
    even_positions = [i for i, x in enumerate(arr) if x % 2 == 0]
    odd_positions = [i for i, x in enumerate(arr) if x % 2 != 0]
    
    even_values = sorted([arr[i] for i in even_positions])
    odd_values = sorted([arr[i] for i in odd_positions], reverse=True)
    
    result = arr[:]
    for i, val in zip(even_positions, even_values):
        result[i] = val
    for i, val in zip(odd_positions, odd_values):
        result[i] = val
    return result

def generate_array(n):
    return np.random.randint(-100, 101, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

sorted_arr = sort_even_odd_separately(arr)
print(f"Mảng sau khi sắp xếp chẵn và lẻ riêng biệt: {sorted_arr}")

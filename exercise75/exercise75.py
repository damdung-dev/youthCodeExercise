from collections import Counter

def find_max_min_frequency_elements(arr):
    frequencies = Counter(arr)
    max_element = max(frequencies, key=frequencies.get)
    min_element = min(frequencies, key=frequencies.get)
    return max_element, min_element

def generate_array(n):
    return [int(x) for x in input(f"Nhập {n} phần tử: ").split()]

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

max_element, min_element = find_max_min_frequency_elements(arr)
print(f"Phần tử xuất hiện nhiều nhất: {max_element}")
print(f"Phần tử xuất hiện ít nhất: {min_element}")

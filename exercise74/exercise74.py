from collections import Counter

def count_element_frequencies(arr):
    return Counter(arr)

def generate_array(n):
    return [int(x) for x in input(f"Nhập {n} phần tử: ").split()]

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

frequencies = count_element_frequencies(arr)
for element, count in frequencies.items():
    print(f"{element}: {count} lần")

def print_unique_elements(arr):
    unique_elements = [x for x in arr if arr.count(x) == 1]
    return unique_elements

def generate_array(n):
    return [int(x) for x in input(f"Nhập {n} phần tử: ").split()]

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

unique_elements = print_unique_elements(arr)
print(f"Các phần tử có trị phân biệt: {unique_elements}")

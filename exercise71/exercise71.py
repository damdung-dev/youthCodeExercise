def is_symmetric(arr):
    return arr == arr[::-1]

def rotate_left(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]

def generate_array(n):
    return [int(x) for x in input(f"Nhập {n} phần tử: ").split()]

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

if is_symmetric(arr):
    print("Mảng đối xứng.")
else:
    print("Mảng không đối xứng.")

k = int(input("Nhập số lần cần dịch trái: "))
rotated_arr = rotate_left(arr, k)
print(f"Mảng sau khi dịch trái {k} lần: {rotated_arr}")

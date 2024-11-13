def find_largest_odd(arr):
    odds = [x for x in arr if x % 2 != 0]
    return max(odds) if odds else None

def rotate_right(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

def generate_array(n):
    return np.random.randint(-100, 101, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

largest_odd = find_largest_odd(arr)
if largest_odd is not None:
    print(f"Số lẻ lớn nhất: {largest_odd}")
else:
    print("Không có số lẻ trong mảng.")

k = int(input("Nhập số lần cần dịch phải: "))
rotated_arr = rotate_right(arr, k)
print(f"Mảng sau khi dịch phải {k} lần: {rotated_arr}")

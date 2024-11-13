import numpy as np

def average_odd_negatives(arr):
    odd_negatives = [x for x in arr if x < 0 and x % 2 != 0]
    if odd_negatives:
        return np.mean(odd_negatives)
    else:
        return None

def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

def generate_array(n):
    return np.random.randint(-100, 101, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

average = average_odd_negatives(arr)
if average is not None:
    print(f"Trung bình cộng các số âm lẻ: {average:.2f}")
else:
    print("Không có số âm lẻ trong mảng.")

arr_no_duplicates = remove_duplicates(arr)
print(f"Mảng sau khi xóa các phần tử trùng nhau: {arr_no_duplicates}")

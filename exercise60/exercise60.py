import numpy as np

def perfect_shuffle(arr):
    mid = len(arr) // 2
    shuffled = [None] * len(arr)
    shuffled[::2] = arr[:mid]
    shuffled[1::2] = arr[mid:]
    return shuffled

def generate_random_array(n):
    return np.random.randint(-100, 101, size=n)

def count_shuffles_until_original(arr):
    original = arr.copy()
    count = 0
    while True:
        count += 1
        arr = perfect_shuffle(arr)
        if np.array_equal(arr, original):
            break
    return count

n = int(input("Nhập n (số chẵn): "))
arr = generate_random_array(n)
print(f"Mảng ban đầu: {arr}")

shuffled = perfect_shuffle(arr)
print(f"Mảng sau khi trộn: {shuffled}")

shuffles_needed = count_shuffles_until_original(arr)
print(f"Số lần trộn để mảng quay về ban đầu: {shuffles_needed}")

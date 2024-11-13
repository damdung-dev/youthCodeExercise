import numpy as np

def longest_increasing_run(arr):
    longest_run = []
    current_run = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            current_run.append(arr[i])
        else:
            if len(current_run) > len(longest_run):
                longest_run = current_run
            current_run = [arr[i]]
    
    if len(current_run) > len(longest_run):
        longest_run = current_run
    
    return longest_run

def generate_array(n):
    return np.random.randint(-100, 101, size=n)

n = int(input("Nhập số phần tử của mảng (1 đến 99): "))
arr = generate_array(n)
print(f"Mảng đã tạo: {arr}")

longest_run = longest_increasing_run(arr)
print(f"'Run' tăng dài nhất: {longest_run}")

import numpy as np

def continuous_square_root(n):
    result = np.sqrt(1)
    for i in range(2, n + 1):
        result = np.sqrt(i + result)
    return result

n = int(input("Nhập n: "))
result = continuous_square_root(n)
print(f"Kết quả của biểu thức: {result:.5f}")

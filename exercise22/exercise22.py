import numpy as np

# Function to find divisors
def find_divisors(n):
    divisors = [i for i in range(1, n+1) if n % i == 0]
    return divisors

# Function to sum the divisors
def sum_divisors(divisors):
    return np.sum(divisors)

# Main program
n = int(input("Nhập số nguyên dương n: "))
divisors = find_divisors(n)

# In kết quả
print(f"Các ước số của {n}: {divisors}")
print(f"Có {len(divisors)} ước số, tổng các ước số là: {sum_divisors(divisors)}")

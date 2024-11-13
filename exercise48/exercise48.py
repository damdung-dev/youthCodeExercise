def largest_odd_divisor(n):
    for i in range(n, 0, -1):
        if n % i == 0 and i % 2 == 1:
            return i

def largest_power_of_2_divisor(n):
    power_of_2 = 1
    while power_of_2 <= n:
        if n % power_of_2 == 0:
            largest = power_of_2
        power_of_2 *= 2
    return largest

n = int(input("Nhập n: "))
odd_divisor = largest_odd_divisor(n)
power_of_2_divisor = largest_power_of_2_divisor(n)

print(f"Ước lẻ lớn nhất: {odd_divisor}")
print(f"Ước lớn nhất là lũy thừa của 2: {power_of_2_divisor}")

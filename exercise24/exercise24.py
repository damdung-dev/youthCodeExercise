import numpy as np

def digit_info(n):
    digits = [int(d) for d in str(n)]
    return len(digits), digits[0], digits[-1], sum(digits), int(str(n)[::-1])

n = int(input("Nhập n: "))
num_digits, first_digit, last_digit, sum_digits, reversed_n = digit_info(n)
print(f"{n} có {num_digits} chữ số")
print(f"Chữ số đầu tiên là: {first_digit}")
print(f"Chữ số cuối cùng là: {last_digit}")
print(f"Tổng các chữ số là: {sum_digits}")
print(f"Số đảo ngược là: {reversed_n}")

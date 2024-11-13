def validate_formula(n):
    left_side = sum([i**2 for i in range(1, n + 1)])
    right_side = n * (n + 1) * (2 * n + 1) // 6
    return left_side, right_side

n = int(input("Nhập n: "))
left, right = validate_formula(n)
print(f"Vế trái: {left}")
print(f"Vế phải: {right}")
print(f"Kết quả đúng: {left == right}")

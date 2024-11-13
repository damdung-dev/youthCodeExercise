def babylonian_sqrt(x):
    y = 1.0
    while abs(y**2 - x) > 1e-5:
        y = (y + x / y) / 2
    return y

x = float(input("Nhập x (x > 0): "))
sqrt_babylonian = babylonian_sqrt(x)
sqrt_builtin = math.sqrt(x)

print(f"Căn bậc hai theo thuật toán Babylonian: {sqrt_babylonian:.5f}")
print(f"Căn bậc hai theo thư viện math: {sqrt_builtin:.5f}")

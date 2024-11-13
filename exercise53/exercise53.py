import math

def sin_taylor(x, precision=1e-4):
    result = 0
    term = x
    n = 1
    while abs(term) >= precision:
        result += term
        term *= -x**2 / ((2*n)*(2*n+1))
        n += 1
    return result

x = float(input("Nhập x (radian): "))
result = sin_taylor(x)
print(f"sin({x}) bằng công thức Taylor: {result:.4f}")
print(f"sin({x}) theo thư viện math: {math.sin(x):.4f}")

from math import gcd

def simplify_fraction(numerator, denominator):
    common_divisor = gcd(numerator, denominator)
    return numerator // common_divisor, denominator // common_divisor

numerator, denominator = map(int, input("Nhập tử số và mẫu số: ").split())
simplified = simplify_fraction(numerator, denominator)
if simplified[1] == 1:
    print(f"Rút gọn: {simplified[0]}")
else:
    print(f"Rút gọn: {simplified[0]}/{simplified[1]}")

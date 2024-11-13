def continued_fraction(s, t):
    fraction = []
    while t != 0:
        a = s // t
        fraction.append(a)
        s, t = t, s % t
    return fraction

s, t = map(int, input("Nhập s và t (0 < s < t): ").split())
fraction = continued_fraction(s, t)
print(f"Phân số liên tục: {fraction}")

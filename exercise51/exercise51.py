def calculate_continued_fraction(x):
    result = 0
    for i in range(1, 6):
        result = i / (2 * result + x)
    return result

x = float(input("Nhập x: "))
result = calculate_continued_fraction(x)
print(f"Giá trị phân số liên tục: {result:.5f}")

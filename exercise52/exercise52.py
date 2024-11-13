def calculate_Fn(n):
    return sum([1 / (i * (i + 1)) for i in range(1, n + 1)])

n = int(input("Nhập n: "))
Fn = calculate_Fn(n)
print(f"Fn = {Fn:.7f}")

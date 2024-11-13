def print_opposite_triangles(n):
    for i in range(1, n + 1):
        print(" ".join(str(j) for j in range(1, i + 1)) + " " * (2 * (n - i) - 1) + " ".join(str(j) for j in range(i, 0, -1)))

n = int(input("Nhập n (n < 5): "))
print_opposite_triangles(n)

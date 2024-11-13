def fibonacci(n):
    if n <= 1:
        return n
    fib_1, fib_2 = 0, 1
    for _ in range(2, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

n = int(input("Nhập n (n < 40): "))
fib_n = fibonacci(n)
print(f"Fibonacci thứ {n}: {fib_n}")

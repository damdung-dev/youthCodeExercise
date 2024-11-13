def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p**2 <= n:
        if primes[p]:
            for i in range(p**2, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]

n = int(input("Nhập n: "))
prime_numbers = sieve_of_eratosthenes(n)

print(f"Các số nguyên tố nhỏ hơn {n}: {prime_numbers}")

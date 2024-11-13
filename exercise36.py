def first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1
    return primes

# Example usage
n = int(input("Enter the number of prime numbers to display: "))
print("First", n, "prime numbers:", first_n_primes(n))

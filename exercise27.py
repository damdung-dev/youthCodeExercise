def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

# Example usage
n = int(input("Enter a positive integer: "))
print("Prime factors:", " * ".join(map(str, prime_factors(n))))

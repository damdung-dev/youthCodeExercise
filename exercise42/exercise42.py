import numpy as np

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_three_primes_sum(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    for p1 in primes:
        for p2 in primes:
            for p3 in primes:
                if p1 + p2 + p3 == n:
                    return (p1, p2, p3)
    return None

def verify_goldbach(limit):
    verified_count = 0
    for n in range(7, limit, 2):
        primes = find_three_primes_sum(n)
        if primes:
            print(f"{n} = {primes[0]} + {primes[1]} + {primes[2]}")
            verified_count += 1
    return verified_count

verified_count = verify_goldbach(1000)
print(f"Số lượng số nguyên tố được kiểm chứng: {verified_count}")

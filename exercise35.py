def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def nearest_prime_below(n):
    if is_prime(n):
        return n
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            return i
    return None

# Example usage
n = int(input("Enter a positive integer: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
    nearest_prime = nearest_prime_below(n)
    print("Nearest prime number below", n, "is:", nearest_prime)

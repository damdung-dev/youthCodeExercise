def divisors_info(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors, len(divisors), sum(divisors)

# Example usage
n = int(input("Enter a positive integer: "))
divisors, count, total = divisors_info(n)
print("Divisors:", divisors)
print("Number of divisors:", count)
print("Sum of divisors:", total)

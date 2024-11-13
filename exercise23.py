def is_perfect(number):
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

def perfect_numbers_below(n):
    return [i for i in range(2, n) if is_perfect(i)]

# Example usage
n = int(input("Enter an integer n: "))
print("Perfect numbers less than", n, ":", perfect_numbers_below(n))

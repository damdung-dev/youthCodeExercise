import math

def combination(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

n, k = map(int, input("Nhập n và k (k < n < 25): ").split())
result = combination(n, k)
print(f"C({n}, {k}) = {result}")

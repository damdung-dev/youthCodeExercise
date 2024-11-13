def largest_m_for_sum(n):
    m = 0
    total_sum = 0
    while total_sum + (m + 1) < n:
        m += 1
        total_sum += m
    return m, total_sum

# Example usage
n = int(input("Enter a positive integer: "))
m, total_sum = largest_m_for_sum(n)
print(f"Largest m such that 1 + 2 + ... + m < {n} is m = {m}")
print("Sum:", total_sum)

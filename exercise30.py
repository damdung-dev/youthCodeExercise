def compound_interest(p, r, n):
    balances = []
    for year in range(1, n + 1):
        a = p * (1 + r) ** year
        balances.append((year, a))
    return balances

# Example usage
p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate (as decimal, e.g., 0.027 for 2.7%): "))
n = int(input("Enter investment period in years: "))

balances = compound_interest(p, r, n)
print("Year | Accumulated Amount")
for year, amount in balances:
    print(f"{year:4} | {amount:.2f}")

import numpy as np

def compound_interest(principal, rate, years):
    return principal * ((1 + rate) ** years)

rate, principal, years = map(float, input("Nhập lãi suất (%), tiền vốn, thời hạn (năm): ").split(','))
rate /= 100
for year in range(1, int(years) + 1):
    amount = compound_interest(principal, rate, year)
    print(f"Year {year}: {amount:.2f}")

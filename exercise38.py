def currency_conversion(amount):
    min_5000 = amount // 5000
    for num_5000 in range(min_5000, -1, -1):
        remaining = amount - num_5000 * 5000
        num_2000 = remaining // 2000
        num_1000 = (remaining % 2000) // 1000
        if num_2000 > (num_2000 + num_1000 + num_5000) / 2:
            return num_1000, num_2000, num_5000
    return None  # No valid solution found

# Example usage
amount = int(input("Enter the amount in thousands of VND: ")) * 1000
result = currency_conversion(amount)
if result:
    num_1000, num_2000, num_5000 = result
    print("1000 VND bills:", num_1000)
    print("2000 VND bills:", num_2000)
    print("5000 VND bills:", num_5000)
else:
    print("No valid solution.")

def custom_round(number, n):
    if n > 0:
        return round(number, n)
    elif n == 0:
        return round(number)
    else:
        factor = 10 ** abs(n)
        return round(number / factor) * factor

# Example usage
number = float(input("Enter a number: "))
precision = int(input("Enter precision n: "))
print("Rounded number:", custom_round(number, precision))

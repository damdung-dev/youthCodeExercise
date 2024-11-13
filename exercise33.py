def is_armstrong(num):
    digits = list(map(int, str(num)))
    power = len(digits)
    return num == sum(digit ** power for digit in digits)

def armstrong_numbers():
    result = []
    for num in range(100, 10000):
        if is_armstrong(num):
            result.append(num)
    return result

# Example usage
print("Armstrong numbers with 3 or 4 digits:", armstrong_numbers())

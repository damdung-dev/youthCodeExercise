def number_properties(n):
    n_str = str(n)
    count_digits = len(n_str)
    last_digit = int(n_str[-1])
    first_digit = int(n_str[0])
    sum_digits = sum(int(digit) for digit in n_str)
    reversed_number = int(n_str[::-1])
    return count_digits, last_digit, first_digit, sum_digits, reversed_number

# Example usage
n = int(input("Enter a positive integer: "))
count, last, first, total, reverse = number_properties(n)
print("Number of digits:", count)
print("Last digit:", last)
print("First digit:", first)
print("Sum of digits:", total)
print("Reversed number:", reverse)

def is_valid_sin(sin):
    sin_str = str(sin)
    if len(sin_str) != 9 or not sin_str.isdigit():
        return "Invalid SIN format"
    
    check_digit = int(sin_str[-1])
    s1 = sum(int(sin_str[i]) for i in range(0, 8, 2))
    s2 = sum(sum(divmod(2 * int(sin_str[i]), 10)) for i in range(1, 8, 2))
    total = s1 + s2
    
    return "Valid SIN" if (total + check_digit) % 10 == 0 else "Invalid SIN"

# Example usage
sin = input("Enter a 9-digit SIN: ")
print(is_valid_sin(sin))

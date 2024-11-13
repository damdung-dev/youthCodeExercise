import math

def simplify_fraction(numerator, denominator):
    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd
    if denominator == 1:
        return numerator
    else:
        return f"{numerator}/{denominator}"

# Example usage
numerator, denominator = map(int, input("Enter the numerator and denominator: ").split())
print("Simplified fraction:", simplify_fraction(numerator, denominator))

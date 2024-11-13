def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def print_conversion_table():
    print("Celsius to Fahrenheit:")
    for c in range(0, 11):
        print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")

    print("\nFahrenheit to Celsius:")
    for f in range(32, 43):
        print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")

# Example usage
print_conversion_table()

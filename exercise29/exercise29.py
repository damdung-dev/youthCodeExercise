import numpy as np

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

print("Celsius to Fahrenheit:")
for c in range(0, 11):
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f:.2f}°F")

print("\nFahrenheit to Celsius:")
for f in range(32, 43):
    c = fahrenheit_to_celsius(f)
    print(f"{f}°F = {c:.2f}°C")

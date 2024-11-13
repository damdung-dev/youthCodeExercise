import numpy as np

def trapezoidal_integration(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    integral = (y[0] + 2 * np.sum(y[1:n]) + y[n]) * h / 2
    return integral

# Function to integrate: f(x) = sin(x) * cos(x)
f = lambda x: np.sin(x) * np.cos(x)

# Limits of integration: from 0 to pi/2
a = 0
b = np.pi / 2

# Precision: n intervals
n = 1000

result = trapezoidal_integration(f, a, b, n)
print(f"Kết quả xấp xỉ tích phân: {result:.6f}")

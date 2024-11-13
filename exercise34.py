import math

def trapezoidal_integral(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    integral *= h
    return integral

# Define the function to integrate
def f(x):
    return math.sin(x) * math.cos(x)

# Approximate with increasing n until accuracy is reached
a = 0
b = math.pi / 2
tolerance = 1e-6
n = 1
while True:
    integral_n = trapezoidal_integral(f, a, b, n)
    integral_2n = trapezoidal_integral(f, a, b, 2 * n)
    if abs(integral_2n - integral_n) < tolerance:
        break
    n *= 2

print("Approximated integral:", integral_2n)

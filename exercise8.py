import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"Linear solution: x = {-c / b}"
    else:
        delta = b**2 - 4 * a * c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return f"Two real solutions: x1 = {x1}, x2 = {x2}"
        elif delta == 0:
            x = -b / (2 * a)
            return f"One real solution: x = {x}"
        else:
            real_part = -b / (2 * a)
            imaginary_part = math.sqrt(-delta) / (2 * a)
            return f"Complex solutions: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i"

# Example usage
a, b, c = map(float, input("Enter coefficients a, b, and c: ").split())
print(solve_quadratic(a, b, c))

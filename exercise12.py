def solve_system(a1, b1, c1, a2, b2, c2):
    D = a1 * b2 - a2 * b1
    if D == 0:
        return "No unique solution"
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1
    x = Dx / D
    y = Dy / D
    return f"x = {x}, y = {y}"

# Example usage
a1, b1, c1 = map(float, input("Enter a1, b1, c1: ").split())
a2, b2, c2 = map(float, input("Enter a2, b2, c2: ").split())
print(solve_system(a1, b1, c1, a2, b2, c2))

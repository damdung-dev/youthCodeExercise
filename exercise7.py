def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        return -b / a

# Example usage
a, b = map(float, input("Enter coefficients a and b: ").split())
solution = solve_linear_equation(a, b)
print("Solution:", solution)

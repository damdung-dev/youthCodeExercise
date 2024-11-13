def sort_three(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

# Example usage
a, b, c = map(int, input("Enter three numbers: ").split())
sorted_numbers = sort_three(a, b, c)
print("Ascending order:", sorted_numbers)

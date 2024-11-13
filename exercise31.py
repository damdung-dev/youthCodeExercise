def print_multiplication_tables():
    for i in range(1, 11):
        row = ""
        for j in range(2, 10):
            row += f"{j} x {i} = {j * i:<3}   "
        print(row)

# Example usage
print_multiplication_tables()


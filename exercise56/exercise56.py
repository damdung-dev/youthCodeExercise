def display_binary_hexadecimal(n):
    binary_representation = bin(n)
    hex_representation = hex(n)
    return binary_representation, hex_representation

n = int(input("Nhập số nguyên n: "))
binary_repr, hex_repr = display_binary_hexadecimal(n)

print(f"{n} = {binary_repr}")
print(f"Hex: {hex_repr.upper()}")

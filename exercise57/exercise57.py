def even_parity_bit(n):
    bit_count = bin(n).count('1')
    return 0 if bit_count % 2 == 0 else 1

n = int(input("Nhập số nguyên n: "))
parity_bit = even_parity_bit(n)

print(f"Even parity bit của {n} = {parity_bit}")

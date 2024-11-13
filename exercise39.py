def pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a + 1, limit):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c < limit:
                c = int(c)
                if (b - a == 1 and c - b == 1) or (a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
                    triplets.append((a, b, c))
    return triplets

# Example usage
limit = 100
print("Pythagorean triplets (consecutive or consecutive even integers):", pythagorean_triplets(limit))

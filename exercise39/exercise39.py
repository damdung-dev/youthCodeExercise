import numpy as np

def find_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit):
        for b in range(a + 1, limit):
            c = np.sqrt(a ** 2 + b ** 2)
            if c.is_integer():
                triples.append((a, b, int(c)))
    return triples

def is_consecutive(triple):
    a, b, c = triple
    return b == a + 1 and c == b + 1

def is_consecutive_even(triple):
    a, b, c = triple
    return a % 2 == 0 and b == a + 2 and c == b + 2

triples = find_pythagorean_triples(100)
consecutive_triples = [t for t in triples if is_consecutive(t)]
even_consecutive_triples = [t for t in triples if is_consecutive_even(t)]

print(f"Ba số nguyên liên tiếp: {consecutive_triples}")
print(f"Ba số chẵn liên tiếp: {even_consecutive_triples}")

def hundred_cows_puzzle():
    solutions = []
    for standing in range(21):
        for lying in range(34):
            old = 100 - standing - lying
            if old >= 0 and 5 * standing + 3 * lying + old / 3 == 100:
                solutions.append((standing, lying, old))
    return solutions

# Example usage
print("Solutions for the 100 cows puzzle:")
for solution in hundred_cows_puzzle():
    print("Standing:", solution[0], ", Lying:", solution[1], ", Old:", solution[2])

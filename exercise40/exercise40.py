def buffalo_puzzle():
    solutions = []
    for standing in range(0, 21):
        for lying in range(0, 34):
            old = 100 - standing - lying
            if old >= 0 and (5 * standing + 3 * lying + old // 3) == 100 and old % 3 == 0:
                solutions.append((standing, lying, old))
    return solutions

solutions = buffalo_puzzle()
for solution in solutions:
    print(f"Trâu đứng: {solution[0]}, Trâu nằm: {solution[1]}, Trâu già: {solution[2]}")

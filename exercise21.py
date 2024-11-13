def entrance_exam(cutoff, scores, region, category):
    region_points = {'A': 2, 'B': 1, 'C': 0.5, 'X': 0}  # X means no priority
    category_points = {1: 2.5, 2: 1.5, 3: 1, 0: 0}      # 0 means no priority
    
    total_score = sum(scores) + region_points.get(region, 0) + category_points.get(category, 0)
    
    if min(scores) == 0:
        return "Fail (a subject has a score of 0)"
    elif total_score >= cutoff:
        return f"Pass! Total score: {total_score}"
    else:
        return f"Fail. Total score: {total_score}"

# Example usage
cutoff = float(input("Enter cutoff score: "))
scores = list(map(float, input("Enter the scores of 3 subjects: ").split()))
region = input("Enter region (A, B, C, X): ").upper()
category = int(input("Enter category (1, 2, 3, 0): "))
print(entrance_exam(cutoff, scores, region, category))

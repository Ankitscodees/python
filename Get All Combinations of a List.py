import itertools
numbers = [1, 2, 3]

combinations = []
for r in range(len(numbers)+1):
    for combination in itertools.combinations(numbers, r):
        combinations.append(combination)

print(combinations)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated = list(zip(*matrix[::-1]))
print("Original Matrix:")
for row in matrix:
    print(row)
print("\nRotated Matrix:")
for row in rotated:
    print(row)

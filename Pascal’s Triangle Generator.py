def generate_pascals_triangle(rows):
    """
    This function generates Pascal's Triangle up to a given number of rows.
    """
    triangle = []

    for i in range(rows):
        # Start each row with 1
        row = [1]
        if i > 0:
            # Fill in the middle values
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            # End each row with 1
            row.append(1)
        triangle.append(row)
    
    return triangle

# Test the function
rows = 5
pascals_triangle = generate_pascals_triangle(rows)
print(f"Pascal's Triangle with {rows} rows:")
for row in pascals_triangle:
    print(row)

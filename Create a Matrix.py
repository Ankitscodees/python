# Python matrix creation
mat = [
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 80]
]

# printing the matrix
print("mat: ", mat)

# printing rows
print("mat[0]: ", mat[0])
print("mat[1]: ", mat[1])
print("mat[2]: ", mat[2])

# printing specific elements
print("mat[0][0]: ", mat[0][0])
print("mat[0][1]: ", mat[0][1])
print("mat[0][2]: ", mat[0][2])
print("mat[1][0]: ", mat[1][0])
print("mat[1][1]: ", mat[1][1])
print("mat[1][2]: ", mat[1][2])
print("mat[2][0]: ", mat[2][0])
print("mat[2][1]: ", mat[2][1])
print("mat[2][2]: ", mat[2][2])

# printing matrix using loop (matrix form)
print("Matrix is: ")
for i in range(3):
  for j in range(3):
    print(mat[i][j], end = " ")
  print() # prints new line

import numpy as np

# Broadcasting

numbers = np.array([4, 5, 6])
print("Matrix + 5: ", numbers+5)

# Aggregation
print("Sum of the matrix: ", numbers.sum())
print("Mean of the matrix: ", numbers.mean())
print("Max of the matrix: ", numbers.max())
print("Min of the matrix: ", numbers.min())
print("Std of the matrix: ", numbers.std())
print("Var of the matrix: ", numbers.var())

# Axis
mtx = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("Matrix: ", mtx.sum(axis=0)) # Sum of the matrix by columns
print("Matrix: ", mtx.sum(axis=1)) # Sum of the matrix by rows
print("Matrix: ", mtx.mean(axis=0)) # Mean of matrix by columns
print("Matrix: ", mtx.mean(axis=1)) # Mean of the matrix by rows

# Reshaping
numbs = np.array([1, 2, 3, 4, 5, 6])
print(numbs.reshape(2, 3))
print(numbs.reshape(3, 2))
print(numbs.reshape(6, 1))
print(numbs.reshape((1, 2, 3)))
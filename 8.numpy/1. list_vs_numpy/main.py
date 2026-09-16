import numpy as np

numbers = [1, 2, 3, 4, 5]
result = [x * 2 for x in numbers]

# print(result)

# With Numpy
numbers = np.array([1, 2, 3, 4, 5])
result = numbers * 2

# print( numbers, result)

# Exercise
numbers = np.array([10, 20, 30, 40, 50])

# 1. Multiply the array by 3
print(numbers * 3)

# 2. Add 5 to each element

print(numbers + 5)

# 3. Get the third element of the array
print(numbers[2])

# 4. Get the elements from the second to the fourth
print(numbers[1:4])
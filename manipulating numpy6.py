Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import numpy as np
# Creating a 1D numpy array
array_1d = np.array([1,2,3,4,5,6])
print("1D Array:")
1D Array:
print(array_1d)
[1 2 3 4 5 6]
# Reshaping the 1D array to a 2x3 2D array
array_2d = array_1d.reshape(2, 3)
print("\nReshaped to 2D Array (2x3):")

Reshaped to 2D Array (2x3):
print(array_2d)
[[1 2 3]
 [4 5 6]]
>>> # Accessing elements using indexing
>>> print("\nElement at position (1, 2):", array_2d[1, 2])

Element at position (1, 2): 6
>>> # Modifying an element
>>> array_2d[0, 1] = 10
>>> print("\nModified Array (After changing element at position (0,1) to 10):")

Modified Array (After changing element at position (0,1) to 10):
>>> print(array_2d)
[[ 1 10  3]
 [ 4  5  6]]
>>> # Calculating the sum of the array elements
>>> array_sum = np.sum(array_2d)
>>> print("\nSum of all elements in the array:", array_sum)

Sum of all elements in the array: 29
>>> import numpy as np
>>> # Creating two matrices
>>> matrix_A = np.array([[1, 2], [3, 4]])
>>> matrix_B = np.array([[5, 6], [7, 8]])
>>> # Matrix Addition
>>> matrix_sum = np.add(matrix_A, matrix_B)
>>> print("Matrix Addition (A + B):")
Matrix Addition (A + B):
>>> print(matrix_sum)
[[ 6  8]
 [10 12]]
>>> # Matrix Multiplication (Element-wise)
>>> matrix_product_elementwise = np.multiply(matrix_A, matrix_B)
>>> print("\nElement-wise Matrix Multiplication (A * B):").
SyntaxError: invalid syntax
>>> print("\nElement-wise Matrix Multiplication (A * B):")

Element-wise Matrix Multiplication (A * B):
>>> print(matrix_product_elementwise)
[[ 5 12]
 [21 32]]
>>> # Matrix Dot Product (Matrix Multiplication)
>>> matrix_dot_product = np.dot(matrix_A, matrix_B)
>>> print("\nMatrix Dot Product (A . B):")

Matrix Dot Product (A . B):
>>> print(matrix_dot_product)
[[19 22]
 [43 50]]

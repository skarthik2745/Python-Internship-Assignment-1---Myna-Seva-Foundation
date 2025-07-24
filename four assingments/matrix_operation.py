# matrix_operations.py
# Program to perform operations on 2x2 matrices using NumPy

import numpy as np

# Define 2x2 matrices A and B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Display original matrices
print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix addition
print("\nMatrix Addition (A + B):\n", A + B)

# Element-wise multiplication
print("\nElement-wise Multiplication (A * B):\n", A * B)

# Matrix multiplication (dot product)
print("\nMatrix Multiplication (A dot B):\n", np.dot(A, B))

# Transpose of Matrix A
print("\nTranspose of Matrix A:\n", A.T)

import numpy as np
matrix = np.array([[1, 2], [3, 4]])
a = np.linalg.inv(matrix)
print("Original Matrix:")
print(matrix)
print("\nInverse Matrix:")
print(a)

#matrix addition
matrix1=np.array([[[2,3,4],[5,7,2],[7,4,3]]])
matrix2=np.array([[[1,7,2],[6,2,9],[3,4,8]]])
print("\n matrix1:")
print(matrix1)
print("\n matrix2:")
print(matrix2)
a=np.add(matrix1,matrix2)
print("\nmatrix addition")
print(a)
#matrix multiplication
a=np.multiply(matrix1,matrix2)
print("\nmatrix multiplication")
print(a)
#matrix substraction
a=np.subtract(matrix1,matrix2)
print("\nmatrix multiplication")
print(a)
#matrix dot product
a=np.dot(matrix1,matrix2)
print("\nmatrix dot product")
print(a)
#Transpose the matrix
matrix=np.array([[2,3],[5,6]])
print("matrix")
print(matrix)
a=np.transpose(matrix)
print("matrix transpose")
print(a)

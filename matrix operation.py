import numpy as np
print("......Array....")
print("\n")
A=np.array([1,2,4,3,2,9])
print("Array=",A)
B= np.array([[5, 8], [3, 1]])
print("\n")
print("matrix =",B)
print("\ntype of matrix",type(B))
print("\n matrix=",B)

print("\n .........dimension........")
print("dimension of matrix A is",A.ndim)
print("dimension of matrix A is",B.ndim)

print("shape(A):",A.shape)
print("shape(B):",B.shape)

print("\n............ arrange...........")
A=np.arange(1,10)
print("A",A)

# print("\nInverse Matrix:")
# print(A)

print("\n......basic arithmetic operation....")
matrix1=np.array([[3,3],[3,2]])
matrix2=np.array([[9,6],[6,8]])
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
print("\nmatrix substraction")
print(a)
print("\n...........matrix dot and Transpose..........")

#Transpose the matrix
matrix1=np.array([[2,3],[5,6]])
matrix2=np.array([[7,3],[2,9]])
print("\n matrix1:")
print(matrix1)
print("\n matrix2:")
print(matrix2)
a=np.dot(matrix1,matrix2)
print("\nmatrix dot product")
print(a)
a=np.transpose(matrix2)
print("\nmatrix transpose")
print(a)

#determinant and inverse
print("\n ..........determinant.................")
matrix=np.array([[[2,4,5],[6,7,2],[5,3,5]]])
print("matrix",matrix)
det=np.linalg.det(matrix)
print("\n",det)
inv=np.linalg.inv(matrix)
print("\n",inv)






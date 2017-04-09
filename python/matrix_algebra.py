import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.matrix([[1], [8], [0], [5]])
alpha = 6



#Matrix Dimensions
print(np.shape(A))
print(np.shape(B))
print(np.shape(C))
print(np.shape(D))
print(np.shape(u))
print(np.shape(w))



#Vector Operations
print(u+v)
print(u-v)
print(alpha * u)
print(np.dot(u,v))
print(np.linalg.norm(u))


#Matrix Operations
print('A + C: not defined')
print(A - np.transpose(C))
print(np.transpose(C) + 3*D)
print(B * A)
print('B * np.transpose(A): not defined')


#Optional
print('BC : not defined')
print(C*B)
print(B**4)
print(A * np.transpose(A))
print(np.transpose(D) * D)
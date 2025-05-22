import numpy as np

A = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]])
b = np.array([[11],[-16],[17]])
#Gauss Jordan
g = np.linalg.solve(A,b)
print('Solucion por Gauss Jordan: ')
print(g)

#Matriz Inversa
A_inv = np.linalg.inv(A)
i = np.matmul(A_inv,b)
print('La Matriz Inversa es:')
print(A_inv)
print('Solución por Matriz Inversa es:')
print(i)

#Método de Cramer
dg = np.linalg.det(A)
print ('La determinante general de A es:',dg)

dx = np.linalg.det([[11,-2,1],[-16,4,-2],[17,-2,4]])
print ('La determinante de dx es: ',dx)

dy = np.linalg.det([[4,11,1],[-2,-16,-2],[1,17,4]])
print ('La determinante de dy es: ',dy)

dz = np.linalg.det([[4,-2,11],[-2,4,-16],[1,-2,17]])
print ('La determinante de dz es: ',dz)

x = dx/dg
y = dy/dg
z = dz/dg
print ('x = ',x)
print ('y = ',y)
print ('z = ',z)

#Método de Descomposición de LU
L = np.zeros((3,3))
U = np.zeros((3,3))

L [0][0] = 1
L [1][1] = 1
L [2][2] = 1

U [0,:] = A [0,:]

L[1][0] = A[1][0]/U[0][0] #l21 = a21/u11
U[1][1] = A[1][1]-L[1][0]*U[0][1] #u22 = a22-l21*u12
U[1][2] = A[1][2]-L[1][0]*U[0][2] #u23=a23-l21*u13
L[2][0] = A[2][0]/U[0][0] #l31 = a31/u11
L[2][1] = (A[2][1]-L[2][0]*U[0][1])/U[1][1]
U[2][2] = A[2][2]-L[2][0]*U[0][2]-L[2][1]*U[1][2]

print('La matriz L es: ')
print(L)

print('La matriz U es: ')
print(U)

print('La multiplicación de L*U es: ')
print(L@U)

#Método Cholesky
C = np.linalg.cholesky(A)
print('La matriz Cholesky es: ')
print(C)
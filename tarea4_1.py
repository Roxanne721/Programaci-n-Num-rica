import numpy as np

A = np.array([[1,2,1],[3,8,1],[0,4,1]])
b = np.array([[2],[12],[2]])
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

dx = np.linalg.det([[2,2,1],[12,8,1],[2,4,1]])
print ('La determinante de dx es: ',dx)

dy = np.linalg.det([[1,2,1],[3,12,1],[0,2,1]])
print ('La determinante de dy es: ',dy)

dz = np.linalg.det([[1,2,2],[3,8,12],[0,4,2]])
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
try:
    C = np.linalg.cholesky(A)
    print('La matriz Cholesky es: ')
    print(C)
except np.linalg.LinAlgError:
    print('El método Cholesky no funciona para esta matriz porque no es definida positiva.')

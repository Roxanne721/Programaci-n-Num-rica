import numpy as np

A = np.array([[1,1,2],[0,1,3],[1,0,-1]])
b = np.array([[-2],[7],[-1]])

error_rel = lambda va,vn: np.abs((va-vn)/va)*100
#Método de Jacobi
x1_v = 0
x2_v = 0
x3_v = 0
n = 3

#x1 = -a12*x2-a13*x3+b1/a11
#x2 = -a21*x1-a23*x3+b2/a22
#x3 = -a31*x1-a32*x2+b3/a33

for i in range(1,n):
    x1 = (-A[0][1]*x2_v-A[0][2]*x3_v+b[0])/A[0][0]
    x2 = (-A[1][0]*x1-A[1][2]*x3_v+b[1])/A[1][1]
    x3 = (-A[2][0]*x1-A[2][1]*x2+b[2])/A[2][2]
    e1 = error_rel(x1_v,x1)
    e2 = error_rel(x2_v,x2)
    e3 = error_rel(x3_v,x3)
    x1_v = x1
    x2_v = x2
    x3_v = x3
    print('Iteración: ',i)
    print('x1 = ',x1)
    print('Error x1 = ',e1)
    print('x2 = ',x2)
    print('Error x2 = ',e2)
    print('x3 = ',x3)
    print('Error x3 = ',e3)
    print('')



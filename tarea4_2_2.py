import numpy as np

A = np.array([[1,-0.1,-0.2],[0.1,7,-0.3],[0.3,-0.2,-10]])
b = np.array([[7.85],[19.3],[71.4]])

x2_v = 0
x3_v = 0
n = 6

#x1 = b1-a12*x2_v-a13*x3_v/a11
#x2 = b2-a21*x1-a23*x3_v/a22
#x3 = b3-a31*x1-a32*x2/a33

for i in range(1,n):
    x1 = (b[0]-A[0][1]*x2_v-A[0][2]*x3_v)/A[0][0]
    x2 = (b[1]-A[1][0]*x1-A[1][2]*x3_v)/A[1][1]
    x3 = (b[2]-A[2][0]*x1-A[2][1]*x2)/A[2][2]
    print('Iteración: ',i)
    print('x1 = ',x1)
    print('x2 = ',x2)
    print('x3 = ',x3)
    print('')
    x2_v = x2
    x3_v = x3
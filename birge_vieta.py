import numpy as np
import matplotlib.pyplot as plt

a = np.array([1,-5,5,-1])
x_i= 0.8

b = np.empty(len(a))
c = np.empty(len(a))

num_iter = 10
n = len(a)
for i in range(1,num_iter+1):
    for j in range(1,n):
        if j == 0:
            b[j] = a[j]
            c[j] = a[j]
        else:
            b[j] = a[j] + x_i*b[j-1]
            c[j] = b[j] + x_i*c[j-1]
        x_i_viejo = x_i
    x_i = x_i_viejo - (b[n-1]/c[n-2])
    print(f'iteracion: {i} \n')
    print(f'xi = {x_i_viejo} \n')
    print(b)
    print(c)

def f(x):
    return np.polyval(a, x)

x = np.linspace(-5, 5, 100)
y = f(x)
plt.plot(x, y, label='f(x)')
plt.plot(x_i, 0, 'ro', label=f'xi = {x_i:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Birge-Vieta')
plt.legend()
plt.grid()
plt.show()
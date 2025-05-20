import numpy as np
import matplotlib.pyplot as plt

a = -3
b = -2
f = lambda x: 2*x*np.cos(2*x) - (x+1)**2

error_rel = lambda va,vn: np.abs((va-vn)/va)*100

xr = -2.1913

xi = b - (f(b)*(a-b))/(f(a)-f(b))
n = 5

for i in range(1,n):
    fa = f(a)
    fxi = f(xi)
    if fa*fxi<0:
        b = xi
    else:
        a = xi
    xi = b - (f(b)*(a-b))/(f(a)-f(b))
    print(f'iteracion {i+1}: a = {a}, b = {b}, raíz = {xi}, error = {error_rel(xr,xi)}')

    
x = np.linspace(-3,3,100)
y= f(x)
plt.plot(x,y)
plt.plot(xi,0,'ro', label=f'xi = {xi:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Falsa Posición')
plt.grid()
plt.show()
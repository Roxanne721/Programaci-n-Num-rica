import numpy as np
import matplotlib.pyplot as plt

a = 3
b = 3.5
f = lambda x: np.cos(x/2)-np.sin(2*x)

error_rel = lambda va,vn: np.abs((va-vn)/va)*100

xr = 3.1416

xi = a+b/2
n = 6

for i in range(1,n):
    fa = f(a)
    fxi = f(xi)
    if fa*fxi<0:
        b = xi
    else:
        a = xi
    xi = (a+b)/2
    print(f'iteracion {i+1}: a = {a}, b = {b}, raíz = {xi}, error = {error_rel(xr,xi)}')

    
x = np.linspace(-5,5,100)
y= f(x)
plt.plot(x,y)
plt.plot(xi,0,'ro', label=f'xi = {xi:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de bisección')
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 8*x*np.sin(x)*np.exp(-x)-1
xc = -0.3
xm1 = 0.5

error_rel = lambda va,vn: np.abs((va-vn)/va)*100

for i in range(5):
    xi = xc - (f(xc)*(xm1-xc))/(f(xm1)-f(xc))
    er = error_rel(xi,xc)
    print(f'iteracion {i+1}: xi = {xi}, error = {error_rel(xi,xc)}')
    xm1 = xc
    xc = xi

x = np.linspace(-1,1,100)
y= f(x)
plt.plot(x,y)
plt.plot(xi,0,'co', label=f'xi = {xi:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Secante')
plt.grid()
plt.show()
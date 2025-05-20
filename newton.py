import numpy as np
import matplotlib.pyplot as plt


f = lambda x: np.cos(x/2) - np.sin(2*x)
df = lambda x: -1/2 * np.sin(x/2) - 2 * np.cos(2*x)

xc = 3.3

error_rel = lambda va, vn: np.abs((va - vn) / va) * 100


for i in range(5):
    xi = xc - (f(xc) / df(xc))
    print(f'iteracion {i+1}: xi = {xi}, error = {error_rel(xi, xc)}')
    xc = xi


x = np.linspace(-5, 5, 100)
y = f(x)
plt.plot(x, y, label='f(x)')
plt.plot(xi, 0, 'ro', label=f'xi = {xi:.4f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Newton-Raphson')
plt.legend()
plt.grid()
plt.show()
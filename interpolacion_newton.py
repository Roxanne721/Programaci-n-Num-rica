import numpy as np #vectores
import matplotlib.pyplot as plt #graficar
import sympy as sp #variables imbolicas, con ellas podemos hacer algebra.

x_valores = np.array([1,4,5,6])
fx = np.log(x_valores)
n = len(x_valores)
b = np.copy(fx)
# 1) Calculo de coeficientes
for k in range(1,n):
  b[k:n] = (b[k:n] - b[k-1])/(x_valores[k:n] - x_valores[k-1])
#2) Construccion del polinomio
x= sp.Symbol('x')
polinomio_newton = b[0] #b0 = f(x0)
for j in range(1,len(x_valores)):
  termino = 1
  for i in range(j):
    termino *= (x-x_valores[i])
  polinomio_newton += b[j]*termino
print(polinomio_newton)
#Convirtiendo el polinomio simbolico a nuerico
polinomio_newton_fun = sp.lambdify(x, polinomio_newton, 'numpy')
#Grafica
eje_x = np.linspace(min(x_valores),max(x_valores),100)
eje_y = polinomio_newton_fun(eje_x)
plt.plot(eje_x,eje_y, label = 'Polinomio de Newton')
plt.plot(x_valores,fx,'o', label = 'Datos originales')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Ejemplo interpolacion de Newton')
plt.grid()
plt.show()
import numpy as np  # Vectores
import matplotlib.pyplot as plt  # Graficar
import sympy as sp  # Variables simbólicas para álgebra

# Datos para la interpolación cuadrática
x_valores = np.array([3, 4, 5])  # Tres puntos para cuadrática
fx = np.log(x_valores)  # Valores de f(x) en los puntos
n = len(x_valores)

# 1) Cálculo de coeficientes de diferencias divididas
b = np.copy(fx)
for k in range(1, n):
    b[k:n] = (b[k:n] - b[k-1]) / (x_valores[k:n] - x_valores[k-1])

# 2) Construcción del polinomio cuadrático
x = sp.Symbol('x')
polinomio_cuadratico = b[0]  # b0 = f(x0)
for j in range(1, n):  # Solo hasta el grado 2
    termino = 1
    for i in range(j):
        termino *= (x - x_valores[i])
    polinomio_cuadratico += b[j] * termino

print("Polinomio cuadrático:", polinomio_cuadratico)

# Convertir el polinomio simbólico a función numérica
polinomio_cuadratico_fun = sp.lambdify(x, polinomio_cuadratico, 'numpy')

# Graficar
eje_x = np.linspace(min(x_valores), max(x_valores), 100)
eje_y = polinomio_cuadratico_fun(eje_x)
plt.plot(eje_x, eje_y, label='Polinomio Cuadrático')
plt.plot(x_valores, fx, 'o', label='Datos Originales')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolación Cuadrática')
plt.legend()
plt.grid()
plt.show()
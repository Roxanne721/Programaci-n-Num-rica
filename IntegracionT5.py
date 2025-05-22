import numpy as np
from sympy import symbols, integrate, cos, exp

x_sim = symbols('x')

f1_sym = 1 - x_sim * cos(x_sim**2)
f2_sym = (-x_sim**2)-x_sim/2+4
f3_sym = exp(-x_sim**2)

# Define the same functions as NumPy-compatible lambda functions for numerical integration
f1 = lambda x: 1-x*np.cos(x**2)
f2 = lambda x: -x**2 - x / 2 + 4
f3 = lambda x: np.exp(-x**2)

#Límites de integración
a = [0, 0.5, 0]
b = [np.pi/4, 1.5, 1]

funciones_sym = [f1_sym, f2_sym, f3_sym]

funciones = [f1, f2, f3]


def simpson_13(f,a,b):
    x1 = (a+b)/2
    I = (b-a)*((f(a)+4*f(x1)+f(b))/6)
    return round(I,4)

print('----------Valores analíticos-------')
x_sim = symbols('x')
for i, funcion_sym in enumerate(funciones_sym):
    integral = integrate(funcion_sym, x_sim)
    print(f'El valor de la integral de la función {i + 1} es: {integral}')
   
# Numerical integration using Simpson's 1/3 rule
print('***Valores Simpson *********\n')
for i in range(len(a)):
    integral_simpson = simpson_13(funciones[i], a[i], b[i])
    print(f'La integral de la función {i + 1} en Simpson 1/3 es: {integral_simpson}')
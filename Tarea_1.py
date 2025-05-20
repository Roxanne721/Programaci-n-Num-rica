import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace, sin, cos, tan
from math import pi

N = int(input("Ingrese un número entero positivo: "))

def multiplos_fila(N, x):
    M = np.array([x * (i + 1) for i in range(N)])
    return M

def multiplos_columna(N, y):
    M = np.array([[y[j] * (i + 1) for j in range(N)] for i in range(N)])
    return M

def grafico():
    x = linspace (0, 2*pi, 100)
    y1 = sin(x)
    y2 = cos(x)
    y3 = tan(x)
    plt.plot(x, y1, 'mp-', label='sin(x)')
    plt.plot(x, y2, 'b|-.', label='cos(x)')
    plt.plot(x, y3, 'cD:', label='tan(x)')
    plt.legend(loc = 'best')
    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.title('Funciones trigonométricas')
    plt.grid()
    plt.show()


if N == int(N) and N >= 1:
    print("Es correcto")
    
    x = np.random.randint(1, 10, N)  
    print("\nVector generado (fila): \n", x)
    print("\nMatriz de multiplicación por fila: \n", multiplos_fila(N, x))

    y = np.random.randint(1, 10, N)
    print("\nVector generado (columna): \n", y)
    print("\nMatriz de multiplicación por columna: \n", multiplos_columna(N, y))

    grafico()


else:
    print("Error")  
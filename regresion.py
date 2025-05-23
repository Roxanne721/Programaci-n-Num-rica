import ssl
#import certifi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv('https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv')
# df.head() # Para ver el contenido de la tabla.
X = df['Experience Years']
Y = df['Salary']

sum_xiyi = sum(X * Y)  # sumatoria de x por y
sum_xi2 = sum(X ** 2)  # sumatoria de x al cuadrado

n = len(X)

a1 = (n * sum_xiyi - sum(X) * sum(Y)) / (n * sum_xi2 - sum(X) ** 2)
a0 = (sum(Y) / n) - a1 * (sum(X) / n)

x_grafica = np.linspace(min(X), max(X), 100)
y_grafica = a0 + a1 * x_grafica
y_regresion = lambda x: a0 + a1 * x
datos_estimar = [15, 30, 50]
for dato in datos_estimar:
    print(f'Años {dato}: salario: {y_regresion(dato)}')

print(f'La función de regresión es {a1}x + {a0}')
plt.plot(x_grafica, y_grafica, label='Línea de regresión')
plt.plot(X, Y, 'o', label='Datos')
plt.xlabel('Experience Years')  # Fixed typo
plt.ylabel('Salary')  # Fixed typo
plt.legend()
plt.grid()
plt.show()
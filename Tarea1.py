"""
import numpy as np

N = int(input("Ingrese un número entero positivo: "))

if N == int(N) and N >= 1:
    print("Es correcto")
    
    x = np.random.randint(1, 10, N)  
    print(x)
    
    v = x
    M = v * np.arange(1, N+1)
    print(M)

else:
    print("Error")
"""

import numpy as np

N = int(input("Ingrese un número entero positivo: "))

if N == int(N) and N >= 1:
    print("Es correcto")
    """Paso 2"""
    x = np.random.randint(1, 10, N)  
    print(x)
    """Paso 3"""
    v = x
    M = np.array([[v[j]*(i+1) for j in range(N)] for i in range(N)])
    print(M)

else:
    print("Error")

#Paso 4

def multiplos_fila(N):
    v = x
    M = v * np.arange(1, N+1)
    print(M)

def multiplos_columna(N):
    v = x
    M = np.array([[v[j]*(i+1) for j in range(N)] for i in range(N)])
    print(M)
    


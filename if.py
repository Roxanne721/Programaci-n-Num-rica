import numpy as np
def multiplos_fila(x):
    """
    Esta función produce una matriz con elemtnos aleatorios en la primera
    fila y después las filas siguientes son múltiplos de la primera 
    Entrada = x es un entero
    Salida = matriz de NxN
    """
    multiplos = np.zeros((x,x))
 
    if x >= 0 and x % 1 == 0: # el porcentaje indica que es entero
        print('Es entero y positivo')
        aleatorio = np.random.randint(low=1, high=9, size=(x,1))
        print(aleatorio)
        for i in range(x): # empieza en 0
            fila = (i+1)*aleatorio
            multiplos[i,:] = fila
            print(multiplos)

    else:
        print('No es entero ni positivo')
    return multiplos


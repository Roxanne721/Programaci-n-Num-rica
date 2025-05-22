import numpy as np
#from scipy.misc import derivative 


fx = lambda x: 1-x*np.cos(x**2)
er = lambda va, vn: np.abs((va - vn) / va) * 100
h = [0.2, 0.1]
xi = 1.8

# Derivación hacia adelante
def derivada_adelante(fx, xi, h):
    fxim1 = fx(xi + h)
    fxim2 = fx(xi + 2 * h)
    return (-fxim2 + 4 * fxim1 - 3 * fx(xi)) / (2 * h)

# Derivación hacia atrás
def derivada_atras(fx, xi, h):
    fxim1 = fx(xi - h)
    fxim2 = fx(xi - 2 * h)
    return (3 * fx(xi) - 4 * fxim1 + fxim2) / (2 * h)

# Derivación centrada
def derivada_centrada(fx, xi, h):
    fxip1 = fx(xi + h)
    fxip2 = fx(xi + 2 * h)
    fxim1 = fx(xi - h)
    fxim2 = fx(xi - 2 * h)
    return (fxip2 + 8 * fxip1 - 8 * fxim1 + fxim2) / (12 * h)

# Print analytical and numerical derivatives
#print('*************************** Valores reales o analíticos ***************************')
#for h_i in h:
#    deriv_analitica = derivative(fx, xi, dx=h_i)  # Use scipy.misc.derivative for analytical derivative
#    print(f'La derivada analítica con h={h_i} es: {deriv_analitica}')

print('*************************** Valores numéricos ***************************')
for h_i in h:
    print(f'h = {h_i}')
    print(f'Derivada hacia adelante con h={h_i} es: {derivada_adelante(fx, xi, h_i)}')
    print(f'Derivada hacia atrás: {derivada_atras(fx, xi, h_i)}')
    print(f'Derivada centrada: {derivada_centrada(fx, xi, h_i)}')
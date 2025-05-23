# Linear Interpolation Example
import numpy as np
import matplotlib.pyplot as plt

xT = [1, 2, 3, 5, 6, 7, 8]
yT = [3, 6, 19, 99, 291, 444]
x = 4
x0 = 3
x1 = 5
y0 = 19
y1 = 99

f = y0 + (((y1-y0)/(x1-x0))*(x-x0))
print ('Los valores de x son:', xT)
print ('Los valores de f(x) son: ', yT)
print ('La interpolación lineal, tomando en cuenta los valores x = 3 y 5, es: ', f)
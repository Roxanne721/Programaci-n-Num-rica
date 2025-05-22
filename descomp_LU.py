import numpy as np

A = np.array([[1,2,1],[3,8,1],[0,4,1]])
b = np.array([[2],[12],[2]])

#resolver el sistema Ax=b
x= np.linalg.solve(A,b)
print(x)

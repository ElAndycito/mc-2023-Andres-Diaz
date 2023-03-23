import numpy as np

# Definimos la matriz de coeficientes y el vector de términos independientes
A = np.array([[1, 1, 0], [3, 3, 4], [4, 1, 0]])
b = np.array([2.5, 11.5, 15])

# Concatenamos la matriz de coeficientes y el vector de términos independientes
AB = np.concatenate((A, np.reshape(b, (3, 1))), axis=1)

# Convertimos la matriz a una forma escalonada reducida mediante la eliminación de Gauss-Jordan
for i in range(AB.shape[0]):
    # Dividimos la fila i por el elemento diagonal
    AB[i,:] = AB[i,:] / AB[i,i]
    # Restamos la fila i multiplicada por el elemento que está debajo del diagonal
    for j in range(i+1, AB.shape[0]):
        AB[j,:] = AB[j,:] - AB[i,:] * AB[j,i]
    # Restamos la fila i multiplicada por el elemento que está encima del diagonal
    for j in range(i):
        AB[j,:] = AB[j,:] - AB[i,:] * AB[j,i]

# La solución son los elementos de la última columna de la matriz AB
x = AB[:, -1]

# Imprimimos la solución
print("La solución del sistema de ecuaciones es:")
print("x1 = {:.2f}".format(x[0]))
print("x2 = {:.2f}".format(x[1]))
print("x3 = {:.2f}".format(x[2]))
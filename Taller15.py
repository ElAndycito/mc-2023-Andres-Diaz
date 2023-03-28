import numpy as np

def gauss_jordan_inverse(matrix):
    # Se crea una matriz aumentada con la matriz original y una matriz identidad del mismo tamaño
    n = len(matrix)
    augmented_matrix = np.concatenate((matrix, np.identity(n)), axis=1)

    # Se realiza la eliminación de Gauss-Jordan para convertir la parte izquierda de la matriz aumentada en una matriz identidad
    for i in range(n):
        # Se intercambian las filas para evitar divisiones por cero
        if augmented_matrix[i][i] == 0:
            for j in range(i+1, n):
                if augmented_matrix[j][i] != 0:
                    augmented_matrix[[i,j]] = augmented_matrix[[j,i]]
                    break
        
        # Se divide la fila i por el elemento diagonal
        diagonal_element = augmented_matrix[i][i]
        augmented_matrix[i] = augmented_matrix[i] / diagonal_element
        
        # Se restan múltiplos de la fila i de las demás filas para eliminar los elementos debajo y encima del elemento diagonal
        for j in range(n):
            if j != i:
                factor = augmented_matrix[j][i]
                augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]

    # La matriz aumentada ha sido convertida en una matriz de la forma [I|A^-1], así que se extrae la matriz inversa
    inverse_matrix = augmented_matrix[:, n:]

    return inverse_matrix
# Matriz A
A = np.array([[3, 2, 2],
              [3, 1, -3],
              [1, 0, -2]])

# Matriz B
B = np.array([[1, 2, 0, 4],
              [1, 0, -1, -2],
              [1, 1, -1, 0],
              [0, 4, 1, 0]])

# Se calcula la inversa de A y B utilizando la función gauss_jordan_inverse
A_inverse = gauss_jordan_inverse(A)
B_inverse = gauss_jordan_inverse(B)

# Se imprimen las matrices inversas
print("Inversa de A:")
print(A_inverse)

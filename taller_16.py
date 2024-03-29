# -*- coding: utf-8 -*-
"""Taller 16

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TJdTOjJHVATjyzNsJmYkz1ZqaepxIEZ3
"""

import numpy as np

# Datos
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([3.5, 2.5, 3, 1.5, 2, 1.3, 1, 0.3])

# Número de elementos
n = len(x)

# Cálculo de los coeficientes de la recta
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x*y)
sum_x2 = np.sum(x*x)

m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
b = (sum_y - m*sum_x) / n

# Print
print("La ecuación de la recta es y = {:.2f}x + {:.2f}".format(m, b))
import numpy as np
import matplotlib.pyplot as plt

# Datos
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([4.2, 1.4, 0, -0.4, -0.1, 1.6, 4.1])

# Ajuste del polinomio de segundo grado
coef = np.polyfit(x, y, 2)
p = np.poly1d(coef)

# Coeficiente de correlación
r = np.corrcoef(x, y)[0, 1]

# Gráfica
plt.scatter(x, y)
plt.plot(x, p(x), color='purple')
plt.title("Ajuste polinómico de segundo grado con r = {}".format(r))
plt.xlabel("x")
plt.ylabel("y")
plt.show()

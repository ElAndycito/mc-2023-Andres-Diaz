import numpy as np
import sympy as sp
from math import e

def RelLin(Lista1,Lista2):
  # Datos
  x = np.array(Lista1)
  y = np.array(Lista2)

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
  print("La ecuación de la recta es y = {:.6f}x + {:.6f}".format(m, b))

def RelNoLin(Lista1,Lista2):
  # Datos
  x = np.array(Lista1)
  y = np.array(Listln(Lista2))

  # Número de elementos
  n = len(x)

  # Cálculo de los coeficientes de la recta
  sum_x = np.sum(x)
  sum_y = np.sum(y)
  sum_xy = np.sum(x*y)
  sum_x2 = np.sum(x*x)

  m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
  b = (sum_y - m*sum_x) / n
  c = e**(m)
  # Print
  print("La ecuación de la exponencial es y = {:.6f}e^{:.6f}x".format(c, m))


def Listln(Lista):
  Lista3 = []
  for i in Lista:
    Lista3.append(sp.ln(i))
  return Lista3



opc = int(input("Ingresa el ejercicio a realizar: "))
if opc == 1:
  Lista1 = [2,4,6,8,10,12]
  Lista2 = [2.2,3,4.5,6,8.5,12]
  RelNoLin(Lista1,Lista2)
elif opc == 2:
  opc2 = int(input("Para reg lineal 1, para reg no lineal 2: "))
  if opc2 == 1:
    cant = int(input("Ingresa la cantidad de datos a ingresar en x: "))
    Lista1 = []
    Lista2 = []
    print("Ingresa todos los datos para las x: ")
    for i in cant:
      Lista1.append()
    print("Ingresa todos los datos para las y: ")
    for i in cant:
      Lista2.append()
    RelLin(Lista1,Lista2)
  elif opc2 == 2:
    cant = int(input("Ingresa la cantidad de datos a ingresar en x: "))
    Lista1 = []
    Lista2 = []
    print("Ingresa todos los datos para las x: ")
    for i in cant:
      Lista1.append()
    print("Ingresa todos los datos para las y: ")
    for i in cant:
      Lista2.append()
    RelNoLin(Lista1,Lista2)
  else:
    print("No existe la opción")
else:
  print("No existe el ejercicio")

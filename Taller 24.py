import numpy as np
import sympy as sp
from math import e
from matplotlib import pyplot
import sys
import matplotlib.pyplot as plt
import statistics
from mpl_toolkits import mplot3d
from sympy import *
import copy
import math

def grafpoli(Lista1,Lista2,xnum,grado,cond):
  x=np.arange(0,20,0.5)
  if cond==1:
    pyplot.plot(x, [seriemultiplic(Lista1,Lista2,i,0) for i in x])
  pyplot.axhline(0, color="black")
  pyplot.axvline(0, color="black")
  pyplot.xlim(-5, 20)
  pyplot.ylim(-5, 20)
  pyplot.plot(np.array(Lista1),np.array(Lista2), "o")
  pyplot.savefig("función.png")
  pyplot.show()
  cont=0
  pyplot.show()

def patronparaseriemultiplic(n,cont2,i):
  if cont2==i:
    cont2=cont2+1
  if cont2>n:
    cont2=0
  return cont2

def seriemultiplic(Lista1,Lista2,xnum,grado):
  x=Symbol("x")
  if grado==0:
    n=len(Lista1)-1
  else:
    n=grado
  cont=1
  cont2=0
  cont3=0
  if n==1:
    for i in range(n+1):
      for j in range(n):
        if i==0:
          cont=cont*((x-Lista1[1])/(Lista1[0]-Lista1[1]))
        if i==1:
          cont=cont*((x-Lista1[0])/(Lista1[1]-Lista1[0]))
        cont=cont*(Lista2[i])
      cont3=cont3+cont
      cont=1
  else:
    for i in range(n+1):
      for j in range(n+1):
        if j!=n:
          cont2=cont2+1
          cont2=patronparaseriemultiplic(n,cont2,i)
          cont=cont*((x-Lista1[cont2])/(Lista1[i]-Lista1[cont2]))
      cont=cont*(Lista2[i])
      cont3=cont3+cont
      cont=1
  if xnum !="no":
    resultado=limit(cont3,x,xnum)
  else:
    resultado=cont3
  return resultado

def operygraf(Lista1,Lista2,xnum,grado,cond):
  if cond==1:
    grafpoli(Lista1,Lista2,xnum,grado,1)
    return seriemultiplic(Lista1,Lista2,xnum,grado)
  else:
    grafpoli(Lista1,Lista2,xnum,grado,2)
    return trazadores(Lista1,Lista2)
  
def trazadores(Lista1,Lista2):
  x=sp.Symbol("x")
  cant=len(Lista1)
  Lista3=[0]
  Lista4=[]
  Lista5=[]
  for i in range(1,cant-3):
    texto="x"+str(i)
    Lista3.append(texto)
    Lista3[i]=sp.Symbol(texto)
    if i==cant-4:
      Lista3.append(0)
  for i in range(1,cant):
    Lista4=[]
    Lista5=[]
    a=((Lista1[i]-Lista1[i-1])*Lista3[i-1])
    b=(2(Lista1[i+1]-Lista1[i-1])*Lista3[i])
    c=((Lista1[i-1]-Lista1[i])*Lista3[i+1])
    d=((6/(Lista1[i+1]-Lista1[i]))*(Lista2[i+1]-Lista2[i]))+((6/(Lista1[i]-Lista1[i-1]))*(Lista2[i-1]-Lista2[i]))
    if a==0:
      Lista4.append([0])
    else:
      Lista4.append([(Lista1[i]-Lista1[i-1])])
    if b==0:
      Lista4.append([0])
    else:
      Lista4.append([2(Lista1[i+1]-Lista1[i-1])])
    if c==0:
      Lista4.append([0])
    else:
      Lista4.append([(Lista1[i-1]-Lista1[i])])
    Lista5.append([d])
  A=np.array(Lista4)
  b=np.array(Lista5)
  AB = np.concatenate((A, b), axis=1)
  for i in range(AB.shape[0]):
    AB[i,:] = AB[i,:] / AB[i,i]
    for j in range(i+1, AB.shape[0]):
        AB[j,:] = AB[j,:] - AB[i,:] * AB[j,i]
    for j in range(i):
        AB[j,:] = AB[j,:] - AB[i,:] * AB[j,i]
  var = AB[:, -1]
  for i in range(1,cant):
    expre=((var[i-1]/(6*(Lista1[i]-Lista1[i-1])))*(Lista1[i]-x)**3)+()+()+()

def gaussJordan(a, b):
  aAux = copy.deepcopy(a)
  bAux = b.copy()

  n = len(bAux)

  #Se construye la matriz triangular superior
  for i in range(n):
    #Pivoteo
    if aAux[i][i] == 0:
      for k in range(i + 1, n):
        if aAux[k][i] != 0:
          filaAux = aAux[i]
          aAux[i] = aAux[k]
          aAux[k] = filaAux

          valoAux = bAux[i]
          bAux[i] = bAux[k]
          bAux[k] = valoAux
          break

    #Escalonamiento
    valorAux = aAux[i][i]
    for j in range(i, n):
      aAux[i][j] /= valorAux
    bAux[i] /= valorAux

    #Reducción
    for j in range(n):
      if j != i:
        fact = aAux[j][i] / aAux[i][i]

        for k in range(n):
          aAux[j][k] -= (aAux[i][k] * fact)
        bAux[j] -= (bAux[i] * fact)
        
  return bAux

x = [0, 1, 2, 3, 4, 5, 6]
y = [3,5,6,5,-2,2,13]

n = len(x)

#se crea la matriz de los trazadores
a = []
b = [0] * (n - 2)
for i in range(n - 2):
  a.append(b.copy())
        
for i in range(1, n - 1):
  if i > 1:
    a[i - 1][i - 2] = x[i] - x[i - 1]
  a[i - 1][i - 1] = 2 * (x[i + 1] - x[i - 1])
  if i < n - 2:
    a[i - 1][i] = x[i + 1] - x[i]
  b[i - 1] = (6 / (x[i + 1] - x[i])) * (y[i + 1] - y[i]) + (6 / (x[i] - x[i - 1]) * (y[i - 1] - y[i]))

rtaAux = gaussJordan(a, b)
f2 = [0] + rtaAux + [0]

for i in range(1, n):
  t1 = f2[i - 1] / (6 * (x[i] - x[i - 1]))
  t2 = f2[i] / (6 * (x[i] - x[i - 1]))
  t3 = y[i - 1] / (x[i] - x[i - 1]) - f2[i - 1] * (x[i] - x[i - 1]) / 6
  t4 = y[i] / (x[i] - x[i - 1]) - f2[i] * (x[i] - x[i - 1]) / 6

  arrCoef = [0] * 4

  #Se calculan los coeficientes del polinomio
  arrCoef[0] = t1 * math.pow(x[i], 3) - t2 * math.pow(x[i - 1], 3) + t3 * x[i] - t4 * x[i - 1]
  arrCoef[1] = -t1 * 3 * math.pow(x[i], 2) + t2 * 3 * math.pow(x[i - 1], 2) - t3 + t4
  arrCoef[2] = t1 * 3 * x[i] - t2 * 3 * x[i - 1]
  arrCoef[3] = -t1 + t2

  print("f(x) = ", end="")
  for j in range(4):
    if arrCoef[j] != 0:
      if j > 0:
        print("+ ", end="")
      print(arrCoef[j], end="")
      if j == 0:
        print(" ", end="")
      elif j == 1:
        print("x ", end="")
      else:
        print("x^" + str(j) + " ", end="")

  print("{x>=" + str(x[i - 1]) + "}{x<" + str(x[i]) + "}")

opc = 1
if opc == 1:
  Lista1=x
  Lista2=y
  xnum=3.25
  grado=0
  resultado1=seriemultiplic(Lista1,Lista2,xnum,grado)
  print("El resultado para el grado 1 es: ","{:.5f}".format(resultado1))

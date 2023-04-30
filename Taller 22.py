import numpy as np
import sympy as sp
from math import e
from matplotlib import pyplot
import sys
import matplotlib.pyplot as plt
import statistics
from mpl_toolkits import mplot3d
from sympy import *

def grafpoli(a,b,cond,Lista1respaldo,Lista2respaldo):
  x=np.arange(0,20,0.5)
  pyplot.plot(x, [formcrec(a,b,i) for i in x])
  pyplot.axhline(0, color="black")
  pyplot.axvline(0, color="black")
  pyplot.xlim(0, 20)
  pyplot.ylim(0, 20)
  pyplot.plot(np.array(Lista1respaldo),np.array(Lista2respaldo), "o")
  if cond==1:
    pyplot.savefig("función_lineal.png")
  elif cond==2:
    pyplot.savefig("función_expo.png")
  elif cond==3:
    pyplot.savefig("función_poten.png")
  elif cond==4:
    pyplot.savefig("función_crec.png")
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
  resultado=limit(cont3,x,xnum)
  return resultado


opc = int(input("Ingrese la opción a revisar: "))
if opc == 1:
  Lista1=[0,1,2,3,4]
  Lista2=[1,0.2,2,4.2,5]
  xnum=2.5
  grado=1
  resultado1=seriemultiplic(Lista1,Lista2,xnum,1)
  print("El resultado para el grado 1 es: ","{:.5f}".format(resultado1))
  resultado2=seriemultiplic(Lista1,Lista2,xnum,2)
  print("El resultado para el grado 2 es: ","{:.5f}".format(resultado2))
  resultado3=seriemultiplic(Lista1,Lista2,xnum,3)
  print("El resultado para el grado 3 es: ","{:.5f}".format(resultado3))
elif opc ==2:
  cant = int(input("Ingresa la cantidad de datos a ingresar en x: "))
  Lista1 = []
  Lista2 = []
  print("Ingresa todos los datos para las x: ")
  for i in range(cant):
    num = float(input(": "))
    Lista1.append(num)
  print("Ingresa todos los datos para las y: ")
  for i in range(cant):
    num = float(input(": "))
    Lista2.append(num)
  grado = int(input("Ingresa el grado a evaluar: "))
  xnum = int(input("Ingresa el x a evaluar: "))
  resultado1=seriemultiplic(Lista1,Lista2,xnum,grado)
  print(resultado1)
  
    
else:
  print("No existe el ejercicio")

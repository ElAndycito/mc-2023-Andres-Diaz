import numpy as np
import sympy as sp
from math import e
from matplotlib import pyplot

def prom(Lista1,Lista2):
  cont=0
  for i in Lista2:
    cont=cont+i
  prome=cont/len(Lista1)
  return prome

def sumatreservdesv(Lista1,Lista2):
  promed=prom(Lista1,Lista2)
  cont=0
  for i in Lista2:
    cont=cont+(i-promed)**2
  sumat = cont
  return sumat

def sumatreserverror(Lista1,Lista2):
  cont=0
  Lista3=RelLin(Lista1,Lista2,2)
  for i in range(len(Lista1)):
    cont=cont+(Lista2[i]-Lista3[0]-(Lista3[1]*Lista1[i]))**2
  sumat = cont
  return sumat

def desvextandar(Lista1,Lista2):
  desv=np.sqrt(sumatreservdesv(Lista1,Lista2)/(len(Lista1)-1))
  print("La desviación estandar es de: ",desv)
  return desv

def errorestantadar(Lista1,Lista2):
  error=np.sqrt(sumatreserverror(Lista1,Lista2)/(len(Lista1)-2))
  print("El error estandar es de: ",error)
  return error

def r(Lista1,Lista2):
  promed=prom(Lista1,Lista2)
  st=sumatreservdesv(Lista1,Lista2)
  sr=sumatreserverror(Lista1,Lista2)
  res=np.sqrt(((st-sr))/st)*100
  print("El r es de: ",res,"%")

def r2(Lista1,Lista2):
  promed=prom(Lista1,Lista2)
  st=sumatreservdesv(Lista1,Lista2)
  sr=sumatreserverror(Lista1,Lista2)
  res=(st-sr)/st
  print("El r2 es de: ",res)

def estadist(Lista1,Lista2):
  print("")
  a=desvextandar(Lista1,Lista2)
  print("")
  b=errorestantadar(Lista1,Lista2)
  print("")
  r(Lista1,Lista2)
  print("")
  r2(Lista1,Lista2)
  print("")
  if a>b:
    print("El modelo es adecuado")




def RelLin(Lista1,Lista2,cond):
  Lista1respaldo=Lista1
  Lista2respaldo=Lista2
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

  a1 = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
  a0 = (sum_y - a1*sum_x) / n
  alfa=a1
  beta=a0

  # Print
  if cond==1:
    print("La ecuación de la recta es y = {:.6f}x + {:.6f}".format(a1, a0))
    print("Su grafica es: ")
    a=alfa
    b=beta
    graf(a,b,1,Lista1respaldo,Lista2respaldo)
  elif cond==2:
    Lista3=[a0,a1]
    return Lista3

def RelNoLin(Lista1,Lista2):
  Lista1respaldo=Lista1
  Lista2respaldo=Lista2
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

  a1 = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
  a0 = (sum_y - a1*sum_x) / n
  alfa = e**(a0)
  beta = a1
  # Print
  print("La ecuación de la exponencial es y = {:.6f}e^{:.6f}x".format(alfa, beta))
  a=alfa
  b=beta
  graf(a,b,2,Lista1respaldo,Lista2respaldo)

def Crecimiento(Lista1,Lista2):
  Lista1respaldo=Lista1
  Lista2respaldo=Lista2
  # Datos
  x = np.array(Listinver(Lista1))
  y = np.array(Listinver(Lista2))

  # Número de elementos
  n = len(x)

  # Cálculo de los coeficientes de la recta
  sum_x = np.sum(x)
  sum_y = np.sum(y)
  sum_xy = np.sum(x*y)
  sum_x2 = np.sum(x*x)

  a1 = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
  a0 = (sum_y - a1*sum_x) / n
  alfa = 1/a0
  beta = a1/a0
  # Print
  print("La ecuación de la razon de crecimiento es y = {:.6f}*x/({:.6f}+x)".format(alfa, beta))
  a=alfa
  b=beta
  graf(a,b,4,Lista1respaldo,Lista2respaldo)

def Potencial(Lista1,Lista2):
  Lista1respaldo=Lista1
  Lista2respaldo=Lista2
  # Datos
  x = np.array(Listlog(Lista1))
  y = np.array(Listlog(Lista2))

  # Número de elementos
  n = len(x)

  # Cálculo de los coeficientes de la recta
  sum_x = np.sum(x)
  sum_y = np.sum(y)
  sum_xy = np.sum(x*y)
  sum_x2 = np.sum(x*x)

  a1 = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
  a0 = sum_y/n - a1*sum_x/n
  alfa = 10**a0
  beta = a1
  # Print
  print("La ecuación de la potencial es y = {:.6f}*x^{:.6f}".format(alfa, beta))
  a=alfa
  b=beta
  graf(a,b,3,Lista1respaldo,Lista2respaldo)

def Listln(Lista):
  Lista3 = []
  for i in Lista:
    Lista3.append(sp.ln(i))
  return Lista3

def Listlog(Lista):
  Lista3 = []
  for i in Lista:
    Lista3.append(sp.log(i,10))
  return Lista3

def Listinver(Lista):
  Lista3 = []
  for i in Lista:
    Lista3.append(1/i)
  return Lista3

def formexp(a,b,x):
  return a*(e**(b*x))

def formpot(a,b,x):
  return a*x**b

def formlin(a,b,x):
  return a*x+b

def formcrec(a,b,x):
  return a*(x/(b+x))

def graf(a,b,cond,Lista1respaldo,Lista2respaldo):
  x=np.arange(0,20,0.5)
  if cond==1:
    pyplot.plot(x, [formlin(a,b,i) for i in x])
  elif cond==2:
    pyplot.plot(x, [formexp(a,b,i) for i in x])
  elif cond==3:
    pyplot.plot(x, [formpot(a,b,i) for i in x])
  elif cond==4:
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


opc = int(input("Ingresa el ejercicio a realizar: "))
if opc == 1:
  Lista1=[1,2,3,4,5,6,7]
  Lista2=[0.2,0.5,1.8,3.4,5.7,9,13.8]
  estadist(Lista1,Lista2)
elif opc == 2:
  opc2 = int(input("Para reg lineal 1, para reg no lineal 2, para potencial 3, para razon de crecimiento 4: "))
  if opc2 == 1:
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
    RelLin(Lista1,Lista2,1)
  elif opc2 == 2:
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
    RelNoLin(Lista1,Lista2)
  elif opc2 == 3:
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
    Potencial(Lista1,Lista2)
  elif opc2 == 4:
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
    Crecimiento(Lista1,Lista2)  
  else:
    print("No existe la opción")
elif opc == 3:
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
  estadist(Lista1,Lista2)
else:
  print("No existe el ejercicio")

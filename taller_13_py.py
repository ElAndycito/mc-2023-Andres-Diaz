import numpy as np
#Resolución de ejercicios... ///
ejercicio = int(input("Ingrese el ejercicio a realizar: "))

if ejercicio==1:
  l=int(input("Ingrese la longitud de los vectores: "))
  A=[]
  B=[]
  for k in range(0,2):
      if k==0:
          print("Ingrese los valores para el vector A")
      else:
          print("Ingrese los valores para el vector B")
      for i in range(0,l):
          num = int(input("Num: "))
          if k==0:
              A.append(num)
          else:
              B.append(num)

elif ejercicio==2:
  #Solicitar las dimensiones al usuario. ///
  filas = int(input('Ingrese el número de filas: '))
  columnas = int(input("Ingrese el número de columnas: "))

  #Matriz de ceros. ///
  matriz = np.zeros((filas, columnas))

  #Valores. ///
  for i in range(filas):
    for j in range(columnas):
      valor = input("Ingrese el valor para la posicion {i}, {j}: ")
      matriz[i, j] = valor

  #ESPACIADO.///
  print("")
  #Print matriz.///
  print(matriz)

  #ESPACIADO.///
  print("")
  # /// Matriz num. 2. ///

  #Solicitar las dimensiones al usuario. ///
  filas2 = int(input('Ingrese el número de filas: '))
  columnas2 = int(input("Ingrese el número de columnas: "))

  #Matriz de ceros. ///
  matriz2 = np.zeros((filas2, columnas2))

  #Valores. ///
  for q in range(filas2):
    for k in range(columnas2):
      valor2 = input("Ingrese el valor para la posicion {i}, {j}: ")
      matriz2[q, k] = valor2

  #ESPACIADO.///
  print("")
  #Print matriz.///
  print(matriz2)

  #ESPACIADO.///
  print("")
  #Operaciones...///
  resultado_a = 3*matriz
  print("Resultado del a: ",resultado_a)

  #ESPACIADO.///
  print("")
  resultado_b = 4*matriz2
  print("Resultado del b: ",resultado_b)

  #ESPACIADO.///
  print("")
  if i!=q or j!=k:
    print("Resultado del c: ERROR!!!.Las matrices no tienen las mismas dimensiones para realizar la suma de las mismas.")
  else:
    resultado_c = matriz + matriz2
    print("Resultado del c: ",resultado_c)

  #ESPACIADO./// #REVISAR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  print("")
  a=np.array([matriz])
  b=np.array([matriz2])
    #Matriz de ceros. ///
  matriz3 = np.zeros((filas, columnas))

  #Valores. ///
  for i in range(filas):
    for j in range(columnas):
      valor=0
      for k in range(columnas):
        a=int(matriz[i,k])
        b=int(matriz2[k,i])
        valor = valor+(a*b)
      matriz3[j, i] = valor
  print("Resultado del d: ",matriz3)


else:
  print("Ejercicio inválido.")

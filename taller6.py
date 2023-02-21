import math

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def erroresp(n):
    es = (0.5*10**-n)*100
    return es

def errorrelat(ac,an):
    ea = abs((ac-an)/ac)*100
    return ea
    
grados = float(input("Ingrese un valor en grados para calcular el coseno: "))
radianes = grados*math.pi/180
resutladoesp = math.cos(radianes)

es=erroresp(8)
ea=100
paso=0
contador=1
contadorit=1
contadorexpo=2

while ea>=es:
    ac = contador
    if paso==0:
        contador = contador-((radianes**contadorexpo)/factorial(contadorexpo))
        paso = paso+1
    else:
        paso = paso-1
        contador = contador+((radianes**contadorexpo/factorial(contadorexpo)))
    an = contador
    ea = errorrelat(ac,an)
    contadorit = contadorit+1
    contadorexpo = contadorexpo+2
    
print("El valor estimnado es de: ",contador)
print("El error aproximado relativo porcentual: ",ea)
print("El número de iteraciones es de: ",contadorit)
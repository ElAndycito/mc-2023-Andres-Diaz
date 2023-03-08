import math

def factorial(x):
    contador=1
    for i in range(0,x):
        contador=contador*(x-i)
    resultado = contador
    return resultado

def errorespe(n):
    Es=(0.5*(10**-n))*100
    return Es

def erroraprox(ac,an):
    Ea=abs(((ac-an)/ac)*100)
    return Ea

x=0.85
resultadoesper = math.e**-0.85
Es = errorespe(8)
Ea = 100
Es2 = errorespe(8)
Ea2 = 100
paso = 0
contador = 1
contadornumit= 1
contadorelevado = 1
contador2 = 1
contadornumit2= 1
contadorelevado2 = 1
contador3 = 1
while Ea>=Es:
    ac = contador
    if paso == 0:
        contador = contador - ((x**contadorelevado)/factorial(contadorelevado))
        paso = paso+1
    else:
        paso = paso-1
        contador = contador + ((x**contadorelevado)/factorial(contadorelevado))
    an = contador
    Ea=erroraprox(ac,an)   
    contadornumit = contadornumit+1
    contadorelevado = contadorelevado+1
while Ea2>=Es2:
    ac2 = contador3
    contador2 = contador2 + ((x**contadorelevado2)/factorial(contadorelevado2))
    contador3 = 1/contador2
    an2 = contador3
    Ea2=erroraprox(ac2,an2)   
    contadornumit2 = contadornumit2+1
    contadorelevado2 = contadorelevado2+1
print("Valor estimado primera ecuación: ",contador)
print("Error aproximador relativo porcentual primera ecuación: ",Ea)
print("Iteraciones primera ecuación: ",contadornumit)
print("--------------------------------------------------------------------")
print("Valor estimado segunda ecuación: ",contador3)
print("Error aproximador relativo porcentual segunda ecuación: ",Ea2)
print("Iteraciones segunda ecuación: ",contadornumit2)

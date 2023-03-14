import math
import sympy as sp
from sympy.solvers import solve
from sympy import Symbol
from sympy import limit, Symbol

def serietaylor(y,x):
    while Ea>=Es:
        ac = contador
        if paso == 0:
            contador = contador - ((radianes**contadorelevado)/factorial(contadorelevado))
            paso = paso+1
        else:
          paso = paso-1
          contador = contador + ((radianes**contadorelevado)/factorial(contadorelevado))
        an = contador
        Ea=erroraprox(ac,an)   
        contadornumit = contadornumit+1
        contadorelevado = contadorelevado+2

def errorespe(n):
    Es=(0.5*(10**-n))*100
    return Es

def factorial(x):
    contador=1
    for i in range(0,x):
        contador=contador*(x-i)
    resultado = contador
    return resultado

def erroraprox(ac,an):
    Ea=abs(((ac-an)/ac)*100)
    return Ea

def serie(xi,xi2,niter,y):
    x = sp.Symbol('x') 
    h=xi2-xi
    cont = 1
    f = y
    Lista = []
    resultado = 0
    for i in range(0,niter):
        ac = cont
        if i == 0:
            cont = cont + limit(f, x, xi)
        else:
            cont = cont + limit((sp.diff(f,x,i)*(h**i))/factorial(i), x, xi)
        an = cont
        if i != 0:
            Ea=erroraprox(ac,an)
            Lista.append(Ea)
    Lista.append(cont)
    return Lista

xi = 0.45 #base
xi2 = 0.455 #x
x=sp.Symbol('x') 
y = math.e**(-x)
niter = 15
Lista = serie(xi,xi2,iter,y)
resultado = Lista[14]
for i in range(0,niter):
    print("El error aproximado relativo porcentual = ",Lista[i])
print("El resultado de euler a la menos x es = ",limit(resultado, x, xi))
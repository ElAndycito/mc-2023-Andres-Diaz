import sympy as sp
import math
from sympy.solvers import solve
from sympy import Symbol
from sympy import limit, Symbol
def factorial(x):
    contador=1
    for i in range(0,x):
        contador=contador*(x-i)
    resultado = contador
    return resultado

def serie(xi,xi2,iter,y):
    x = sp.Symbol('x') 
    h=xi2-xi
    cont = 0
    f = y
    a = ""
    resultado = 0
    for i in range(0,iter):
        if i != 0:
            cont = cont + f
        else:
            cont = cont + (sp.diff(f,x,i)*(h**i))/factorial(i)
    resultado = cont
    return resultado

opc = int(input("Ingrese el ejercicio a revisar o 3 para uno propio: "))

if opc == 1:
    xi = 0.5
    xi2 = 0.6
    x=sp.Symbol('x') 
    y = 1.1*(x**3)-1.6*(x**2)+3*x-5
    iter = 10
    resultado = serie(xi,xi2,iter,y)
    print(limit(resultado, x, xi)/10)
elif opc == 2:
    xi = 0.4
    xi2 = 0.45
    x=sp.Symbol('x') 
    y = 1.6*(math.e**x)-4.2*x+2.75
    iter = 10
    resultado = serie(xi,xi2,iter,y)
    print(limit(resultado, x, xi)/10)
elif opc == 3:
    xi = float(input("Ingrese el x inicial: ")) 
    xi2 = float(input("Ingrese el x final: ")) 
    x=sp.Symbol('x') 
    y = input("Ingrese la función a evaluar: ")
    iter = float(input("Ingrese el número de iteraciones: ")) 
    resultado = serie(xi,xi2,iter,y)
    print(limit(resultado, x, xi)/10)
else:
    print("La opción no existe")
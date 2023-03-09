import sympy as sp
import math
from sympy.solvers import solve
from sympy import Symbol
from sympy import limit, Symbol

def progerror(xaprox,xerror,y):
    x = sp.Symbol('x') 
    error = [xaprox-xerror,xaprox+xerror]
    fd =  (sp.diff(y,x,1))
    fxaprox = abs(limit(fd, x, xaprox)*xerror)
    resultado = [limit(y, x, xaprox)-fxaprox,limit(y, x, xaprox)+fxaprox]
    return resultado

opc = int(input("Ingrese el ejercicio a revisar o 3 para uno propio: "))

if opc == 1:
    xaprox = 1.25
    xerror = 0.05
    x=sp.Symbol('x') 
    y = (1.1*(x**4))-(2.2*(x**3))+(0.7*(x**2))-(2*x)+2
    resultado = progerror(xaprox,xerror,y)
    print(resultado)
elif opc == 2:
    xaprox = math.pi/3
    xerror = 0.005
    x=sp.Symbol('x') 
    y = sp.cos(x)*sp.ln(2*x)
    resultado = progerror(xaprox,xerror,y)
    print(resultado)
elif opc == 3:
    xaprox = float(input("Ingrese el x aproximado: ")) 
    xerror = float(input("Ingrese el x errpr: ")) 
    x=sp.Symbol('x') 
    y = input("Ingrese la función a evaluar: ")
    resultado = progerror(xaprox,xerror,y)
    print(resultado)
else:
    print("La opción no existe")
def factorial(x):
    contador=1
    for i in range(0,x):
        contador=contador*(x-i)
    resultado=contador
    return resultado

def permutacion(n,r):
    perm=factorial(n)/factorial(n-r)
    return perm

def combinacion(n,r):
    comb=factorial(n)/(factorial(r)*factorial(n-r))
    return comb

ejercicio = int(input("Seleccione un ejercicio a ver el resultado de 1 al 2: "))
if ejercicio == 1: 
    print("Resultado del a: ")
    a = combinacion(18,8)
    print(a)
    print("Resultado del b: ")
    b = combinacion(5,3)
    c = combinacion(13,5)
    d = b*c
    print(d)

elif ejercicio==2:
    print("Resultado de a:")
    a = combinacion(52,5)
    print(a)
    print("Resultado de b:")
    b = (permutacion(13,5)/factorial(5))
    print("Resultado de c:")
    c = combinacion(4,3)
    d = combinacion(4,2)
    e = c*d*13*12
    print(e)

else:
    print("Número inválido.")

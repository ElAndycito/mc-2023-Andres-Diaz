def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def permutacion(n,r):
    perm=factorial(n)/factorial(n-r)
    
def combinacion(n,r):
    comb=factorial(n)/(factorial(r)*factorial(n-r))
    
def teoremamultiplic(Lista,cant):
    cont=1
    for i in range(cant):
        cont=cont*Lista[i]
    resultado = cont
    return resultado

ejercicio=int(input("Seleccione un ejercicio a ver el resultado de 1 al 6: "))
if ejercicio==1:
    print("Resultado del ejercicio 1a: ")
    Lista=[3,5,3,2]
    cant=4
    a = teoremamultiplic(Lista,cant)
    print(a)
    print("Resultado del ejercicio 1b: ")
    Lista=[10,5,3,2]
    cant=4
    b = teoremamultiplic(Lista,cant)
    print(b)

elif ejercicio == 2: 
    print("Resultado del primero: ")
    Lista=[26,26,26,10,10,10]
    cant=6
    a = teoremamultiplic(Lista,cant)
    print(a)
    print("Resultado del segundo: ")
    Lista=[26,25,24,10,9,8]
    cant=6
    b = teoremamultiplic(Lista,cant)
    print(b)
    
elif ejercicio == 3: 
    print("Resultado: ")
    Lista=[2,2,2,2,2,2,2,2,2,2,2,2]
    cant=12
    a = teoremamultiplic(Lista,cant)
    print(a)
    
elif ejercicio == 4: 
    print("No existe en las diapositivas")
    
elif ejercicio == 5: 
    print("Resultado: ")
    a = permutacion(12,4)
    print(a)
    
elif ejercicio == 6: 
    print("Resultado del a: ")
    a = factorial(9)
    print(a)
    print("Resultado del b: ")
    b = permutacion(9,5)
    print(b)
    print("Resultado del c: ")
    Lista=[5,4,4,3,3,2,2]
    cant=7
    c = teoremamultiplic(Lista,cant)
    print(c)
    
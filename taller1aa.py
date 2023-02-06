Conjunto_1 = []
Conjunto_2 = []
Conjunto_3 = []
Conjunto_4 = []
Conjunto_5 = []
Conjunto_6 = []
#0=si 1=no
x=0
condition=1
while x==0:
    print("Elije la opción correspondiente: ")
    a=int(input("1) Agregar al counjunto 1  ||  2) Agregar al conjunto 2  ||  0) TERMINAR"))
    if a==1:
        b=float(input("Ingrese el número a agregar: "))
        for i in Conjunto_1:
            if b==i:
                condition=0
        if condition==0:
            print("El número ya se encuentra en el conjunto.")
        else:
            Conjunto_1.append(b)
    elif a==2:
        b=float(input("Ingrese el número a agregar: "))
        for i in Conjunto_2:
            if b==i:
                cond=0
        if cond==0:
            print("El número ya se encuentra en el conjunto.")
        else:
            Conjunto_2.append(b)
    elif a==0:
        x=1
    else:
        print("OPCIÓN NO VÁLIDA!")
    cond=1

def union(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6):
    aea=1
    for i in Conjunto_1:
        for k in Conjunto_3:
            if k==i:
                aea=0
        if aea==0:
            pass
        elif aea==1:
            Conjunto_3.append(i)
        aea=1
    for i in Conjunto_2:
        for k in Conjunto_3:
            if k==i:
                aea=0
        if aea==0:
            pass
        elif aea==1:
            Conjunto_3.append(i)
        aea=1
    return Conjunto_3
def inter(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6):
    aea=1
    for i in Conjunto_1:
        for k in Conjunto_2:
            if k==i:
                aea=0
        if aea==0:
            Conjunto_4.append(i)
        aea=1
    return Conjunto_4
def dif(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6):
    aea=1
    Conjunto_5=Conjunto_1
    for i in Conjunto_1:
        for k in Conjunto_2:
            if k==i:
                aea=0
        if aea==0:
            Conjunto_5.remove(i)
        aea=1
    return Conjunto_5
def difsim(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6):
    a=union(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6)
    b=inter(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6)
    Conjunto_6=dif(Conjunto_3,Conjunto_4,Conjunto_1,Conjunto_2,Conjunto_5,Conjunto_6)
    return Conjunto_6

print("Ingrese la operación a realizar: ")
op=int(input("1) UNION  ||  2) INTERSECCIÓN  ||  3) DIFERENCIA  ||  4) DIFERENCIA SIMÉTRICA"))
if op==1:
    resultado = union(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6)
    print(resultado)
    print("Su cardianlidad es de: ",len(resultado))
elif op==2:
    resultado = inter(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6)
    print(resultado) 
    print("Su cardianlidad es de: ",len(resultado))
elif op==3:
    resultado = dif(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6)
    print(resultado) 
    print("Su cardianlidad es de: ",len(resultado))
elif op==4:
    resultado = difsim(Conjunto_1,Conjunto_2,Conjunto_3,Conjunto_4,Conjunto_5,Conjunto_6)
    print(resultado) 
    print("Su cardianlidad es de: ",len(resultado))
else:
    print("OPCIÓN NO VÁLIDA!")
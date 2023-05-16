#REALIZAR LA GRÁFICA EN DESMOS PARA VER LAS RAÍCES Y COMPARAR AL FINAL LOS RESULTADOS DE LAS RAÍCES.
#Función
def f(x):
    return 1.5 * x**3 - 3.5 * x**2 - 2 * x + 2

#Método de bisección.
def bisection(a, b, tol=1e-8, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
      #Exception 1
        raise ValueError("La función no cruza el eje x en el intervalo dado")
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        if abs(fc) < tol: #Tolerancia max. para el Error aprox.
            return c, abs(b - a) / 2**i, i
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
            #Exception 2
    raise RuntimeError("El método de la bisección no converge en el número máximo de iteraciones")

#a y b son los límites del intervalo elegidos por nosotros (uno debe ser positivo en la función y el otro negativo)
a = 0
b = 1
root, error, iterations = bisection(a, b)
print(f"La raíz aproximada es {root:.8f}, con un error aproximado de {error:.8f} y se realizaron {iterations} iteraciones.")

import math

def f(x):
    return x**2 - math.exp(-2*x) - 3

def f_prime(x):
    return 2*x + 2*math.exp(-2*x)

def newton_raphson(x0, tol=1e-8, max_iter=100):
    for i in range(max_iter):
        fx = f(x0)
        fx_prime = f_prime(x0)
        x1 = x0 - fx / fx_prime
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    print("No se ha encontrado una raíz con la precisión deseada después de", max_iter, "iteraciones.")
    return None
  
x0 = 1.0  # Estimación inicial
raiz = newton_raphson(x0)
print("La raíz estimada es:", round(raiz, 8))

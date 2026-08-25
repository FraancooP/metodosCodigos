import math


def f(x: float) -> float:
    #return x**3 - 13*x**2 + 40*x - 25
    return 30*x**2-x**3-2552
    #return x*math.cosh((12)/x) - x - 5
def fprima(x: float) -> float:
    h = 0.001
    return (f(x + h) - f(x)) / h
limite = 1000
tolerancia = 1e-5
error = float("inf")
i = 0
x0 = 5
xviejo = x0
while error > tolerancia and i < limite:
    i += 1
    derivada = fprima(xviejo)
    if abs(derivada) < 0.0001:
        print("Derivada muy pequeña, el método no puede continuar")
        exit()
    xnuevo = xviejo - f(xviejo) / derivada
    error = abs(xnuevo - xviejo)
    xviejo = xnuevo

print("Mostrando resultados (Newton-Raphson):")
print("Iteraciones:", i)
print("Raíz:", xviejo)
print("Error:", error)
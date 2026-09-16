import math


def f(x: float) -> float:
    #return x**3 - 13*x**2 + 40*x - 25
    return (math.sin(3*x) - math.log10(x)) / 2
    #return x*math.cosh((12)/x) - x - 5
def fprima(x: float) -> float:
    h = 0.01
    return (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2*h)
limite = 1000
tolerancia = 1e-6
error = float("inf")
i = 0
x0 = 0.5
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
print("Error absoluto estimado:", error)
if xviejo != 0:
    error_porcentual_estimado = (error / abs(xviejo)) * 100
    print("Error porcentual estimado:", error_porcentual_estimado, "%")
else:
    print("Error porcentual estimado: no definido, raiz = 0.")
print("Residuo |f(raiz)|:", abs(f(xviejo)))

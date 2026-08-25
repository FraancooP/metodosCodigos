import math


def f(x: float) -> float:
    #return x**2 - 2
    return x**3 - 13*x**2 + 40*x - 25
limite = 1000
xviejo = 0.1
xviejoviejo = 1
tolerancia = 1e-5
error = float("inf")
i = 0
while error > tolerancia and i < limite:
    i += 1
    xnuevo = xviejo - ((f(xviejo) * (xviejoviejo - xviejo)) / (f(xviejoviejo) - f(xviejo)))
    error = abs(xnuevo - xviejo)
    xviejoviejo = xviejo
    xviejo = xnuevo
print("Mostrando resultados (Secante):")
print("Iteraciones:", i)
print("Raíz:", xviejo)
print("Error:", error)
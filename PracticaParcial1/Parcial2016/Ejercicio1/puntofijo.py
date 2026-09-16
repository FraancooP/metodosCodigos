import math


def g(x: float) -> float:
    #return math.exp(-math.exp(math.sin(x)))
    #return math.exp(-x)
    #return math.cos(math.sin(x))
    #return x**(x-math.cos(x))
    #return (13*x**2 - x**3 + 25)/40
    return (math.sin(3*x) - math.log10(x)) / 2

def gprima(x: float) -> float:
    h = 0.001
    return (g(x + h) - g(x)) / h

tolencia = 1e-6
error = float("inf")#Declaro infitino positivo, es para que sea verdadera al comenzar
i = 0
x0 = 0.5
xviejo = x0
while error > tolencia:
    i += 1
    if abs(gprima(xviejo)) > 1:
        print("El metodo no converge")
        exit()
    xnuevo = g(xviejo)
    error = abs(xnuevo - xviejo)
    xviejo = xnuevo

print("Mostrando Resultados(Punto fijo): ")
print("Iteraciones: ", i)
print("Raiz: ", xnuevo)
print("Error absoluto estimado: ", error)
if xnuevo != 0:
    error_porcentual_estimado = (error / abs(xnuevo)) * 100
    print("Error porcentual estimado: ", error_porcentual_estimado, "%")
else:
    print("Error porcentual estimado: no definido, raiz = 0.")
print("Residuo |g(raiz) - raiz|: ", abs(g(xnuevo) - xnuevo))

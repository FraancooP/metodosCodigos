import math


def funcion(x: float) -> float:
    #return math.log(x) + pow(math.e, math.sin(x)) - x
    #return -2 + 7 * x - 5 * pow(x, 2) + 6 * pow(x, 3)
    #return pow(x, 10) - 1
    #return ((9.81 * x) / 14)*(1 - pow(math.e, (-14 / x) * 7)) - 35
    #return (math.log(x) - 1 + (1/x))/(math.log(x) + ((1-(1/x))/0.67)) - 0.3
    #return math.exp(x**2) - 2
    return -15.331539 + 58.603579*x - 74.220198*x**2 + 30.950396 *x**3
    
    
a = float(input("Ingrese inicio intervalo: "))
b = float(input("Ingrese fin intervalo: "))
tolencia = 1e-8
error = float("inf")#Declaro infitino positivo, es para que sea verdadera al comenzar

i = 0
if funcion(a) * funcion(b) > 0:
    print("El intervalo no es valido")
    exit()
    

while error > tolencia:
    i += 1
    cnuevo = (a + b) / 2
    m = funcion(cnuevo)*funcion(b)
    if(i>1):
        error = abs(cnuevo - cviejo)
    if m < 0:
        a = cnuevo
    elif m > 0:
        b = cnuevo
    elif m == 0:
        break
    #print(error)
    
    cviejo = cnuevo

print("Mostrando Resultados(Biseccion): ")
print("Iteraciones: ", i)
print("Raiz: ", cnuevo)
print("Error: ", error)    
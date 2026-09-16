import math
from PracticaParcial1.Parcial2016.Ejercicio3.gausspivoteo import gauss_pivoteo


# --------------------------------------------------
# 1. LEER LOS DATOS
# --------------------------------------------------

cantidad = int(input("Ingrese la cantidad de puntos: "))

if cantidad < 2:
    raise SystemExit("Se necesitan al menos dos puntos.")

datos_x = []
datos_y = []

for i in range(cantidad):
    xi = float(input(f"Ingrese x{i}: ").replace(",", "."))
    yi = float(input(f"Ingrese y{i}: ").replace(",", "."))

    datos_x.append(xi)
    datos_y.append(yi)


# --------------------------------------------------
# 2. ELEGIR EL GRADO
# --------------------------------------------------

grado = int(input("\nIngrese el grado del polinomio: "))

if grado < 1:
    raise SystemExit("El grado debe ser al menos 1.")

if cantidad < grado + 1:
    raise SystemExit("No hay suficientes datos para ese grado.")

# set elimina valores repetidos.
if len(set(datos_x)) < grado + 1:
    raise SystemExit("No hay suficientes valores distintos de x.")


# --------------------------------------------------
# 3. ARMAR LAS ECUACIONES NORMALES
# --------------------------------------------------

A = []
b = []

for fila in range(grado + 1):

    # b[fila] = suma de y[i] * x[i]**fila
    suma_xy = 0.0

    for i in range(cantidad):
        suma_xy += datos_y[i] * datos_x[i] ** fila

    b.append(suma_xy)

    # Construir una fila de la matriz.
    fila_A = []

    for columna in range(grado + 1):

        # A[fila][columna] = suma de x[i]**(fila + columna)
        suma_x = 0.0

        for i in range(cantidad):
            suma_x += datos_x[i] ** (fila + columna)

        fila_A.append(suma_x)

    A.append(fila_A)


# --------------------------------------------------
# 4. MOSTRAR Y RESOLVER EL SISTEMA
# --------------------------------------------------

print("\nMatriz A:")

for fila in A:
    print(fila)

print("\nVector b:")
print(b)

coeficientes = gauss_pivoteo(A, b)

print("\nCoeficientes:")

for i in range(grado + 1):
    print(f"a{i} = {coeficientes[i]:.12g}")


# --------------------------------------------------
# 5. MOSTRAR EL POLINOMIO
# --------------------------------------------------

polinomio = f"{coeficientes[0]:.12g}"

for i in range(1, grado + 1):

    if coeficientes[i] >= 0:
        signo = "+"
    else:
        signo = "-"

    if i == 1:
        potencia = "x"
    else:
        potencia = f"x**{i}"

    polinomio += (
        f" {signo} {abs(coeficientes[i]):.12g}*{potencia}"
    )

print("\nPolinomio ajustado:")
print("F(x) =", polinomio)


# --------------------------------------------------
# 6. CALCULAR PREDICCIONES, Sr Y St
# --------------------------------------------------

promedio_y = sum(datos_y) / cantidad

sr = 0.0
st = 0.0

print("\nComparacion con los datos:")

for i in range(cantidad):

    prediccion = 0.0

    for j in range(grado + 1):
        prediccion += coeficientes[j] * datos_x[i] ** j

    residuo = prediccion - datos_y[i]

    sr += residuo ** 2
    st += (datos_y[i] - promedio_y) ** 2

    print(
        f"x = {datos_x[i]:.6g} | "
        f"y = {datos_y[i]:.6g} | "
        f"F(x) = {prediccion:.8f} | "
        f"residuo = {residuo:.8f}"
    )

print(f"\nPromedio de y = {promedio_y:.12g}")
print(f"Sr = {sr:.12g}")
print(f"St = {st:.12g}")


# --------------------------------------------------
# 7. CALCULAR LA CALIDAD DEL AJUSTE
# --------------------------------------------------

if max(datos_y) == min(datos_y):
    print("Todos los valores de y son iguales.")
    print("R^2 y el r del apunte no estan definidos: St = 0.")
else:
    r_cuadrado = 1 - sr / st

    print(f"R^2 = {r_cuadrado:.12g}")

    if r_cuadrado >= 0:
        r_apunte = math.sqrt(r_cuadrado)
        print(f"r del apunte = sqrt(R^2) = {r_apunte:.12g}")
    else:
        print("R^2 resulto negativo: revisar la precision y la resolucion.")


# --------------------------------------------------
# 8. EVALUAR EL POLINOMIO EN UN PUNTO
# --------------------------------------------------

x_evaluar = float(
    input("\nIngrese el valor de x que desea evaluar: ")
    .replace(",", ".")
)

resultado = 0.0

for i in range(grado + 1):
    resultado += coeficientes[i] * x_evaluar ** i

print(f"\nF({x_evaluar}) = {resultado:.12g}")
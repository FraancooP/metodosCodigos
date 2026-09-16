import math
from gausspivoteo import gauss_pivoteo


# --------------------------------------------------
# 1. DEFINIR LAS FUNCIONES DEL MODELO
# --------------------------------------------------

# F(x) = a0 * sen(x) + a1 * exp(x)

cantidad_coeficientes = 2


def base(k, x):
    if k == 0:
        return math.sin(x)
    elif k == 1:
        return math.exp(x)
    else:
        raise ValueError("No existe una base para ese indice.")
    


# --------------------------------------------------
# 2. LEER LOS DATOS
# --------------------------------------------------

cantidad = int(input("Ingrese la cantidad de puntos: "))

if cantidad < cantidad_coeficientes:
    raise SystemExit("No hay suficientes datos.")

datos_x = []
datos_y = []

for i in range(cantidad):
    xi = float(input(f"Ingrese x{i}: ").replace(",", "."))
    yi = float(input(f"Ingrese y{i}: ").replace(",", "."))

    datos_x.append(xi)
    datos_y.append(yi)


# --------------------------------------------------
# 3. ARMAR LA MATRIZ A Y EL VECTOR b
# --------------------------------------------------

A = []
b = []

for fila in range(cantidad_coeficientes):

    # b[fila] = suma de y[i] * base_fila(x[i])
    suma_y = 0.0

    for i in range(cantidad):
        suma_y += datos_y[i] * base(fila, datos_x[i])

    b.append(suma_y)

    fila_A = []

    for columna in range(cantidad_coeficientes):

        # A[fila][columna] = suma de productos de bases
        suma = 0.0

        for i in range(cantidad):
            suma += (
                base(fila, datos_x[i])
                * base(columna, datos_x[i])
            )

        fila_A.append(suma)

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

for i in range(cantidad_coeficientes):
    print(f"a{i} = {coeficientes[i]:.12g}")

print("\nModelo ajustado:")
print(
    f"F(x) = ({coeficientes[0]:.12g})*sin(x)"
    f" + ({coeficientes[1]:.12g})*exp(x)"
)


# --------------------------------------------------
# 5. CALCULAR PREDICCIONES Y RESIDUOS
# --------------------------------------------------

sr = 0.0
st = 0.0
promedio_y = sum(datos_y) / cantidad

print("\nComparacion con los datos:")

for i in range(cantidad):

    prediccion = 0.0

    for k in range(cantidad_coeficientes):
        prediccion += (
            coeficientes[k] * base(k, datos_x[i])
        )

    residuo = prediccion - datos_y[i]

    sr += residuo ** 2
    st += (datos_y[i] - promedio_y) ** 2

    print(
        f"x = {datos_x[i]:.6g} | "
        f"y = {datos_y[i]:.6g} | "
        f"F(x) = {prediccion:.8f} | "
        f"residuo = {residuo:.8f}"
    )

print(f"\nSr = {sr:.12g}")
print(f"St = {st:.12g}")

if max(datos_y) == min(datos_y):
    print("R^2 no esta definido: todos los y son iguales.")
else:
    r_cuadrado = 1 - sr / st
    print(f"R^2 = {r_cuadrado:.12g}")


# --------------------------------------------------
# 6. EVALUAR EL MODELO EN UN PUNTO
# --------------------------------------------------

x_evaluar = float(
    input("\nIngrese el valor de x que desea evaluar: ")
    .replace(",", ".")
)

resultado = 0.0

for k in range(cantidad_coeficientes):
    resultado += coeficientes[k] * base(k, x_evaluar)

print(f"\nF({x_evaluar}) = {resultado:.12g}")
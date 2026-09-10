from gausspivoteo import gauss_pivoteo


# --------------------------------------------------
# 1. LEER LOS DATOS
# --------------------------------------------------

cantidad = int(input("Ingrese la cantidad de puntos: "))

datos_x = []
datos_y = []

for i in range(cantidad):
    xi = float(input(f"Ingrese x{i}: ").replace(",", "."))
    yi = float(input(f"Ingrese y{i}: ").replace(",", "."))

    datos_x.append(xi)
    datos_y.append(yi)


# --------------------------------------------------
# 2. ARMAR LA MATRIZ A Y EL VECTOR b
# --------------------------------------------------

A = []
b = datos_y[:]

for i in range(cantidad):
    fila = []

    for j in range(cantidad):
        fila.append(datos_x[i] ** j)

    A.append(fila)


# --------------------------------------------------
# 3. MOSTRAR LOS DATOS
# --------------------------------------------------

print("\nDatos ingresados:")

for i in range(cantidad):
    print(f"(x{i}, y{i}) = ({datos_x[i]}, {datos_y[i]})")

print("\nMatriz A:")

for fila in A:
    print(fila)

print("\nVector b:")
print(b)


# --------------------------------------------------
# 4. RESOLVER EL SISTEMA CON GAUSS
# --------------------------------------------------

coeficientes = gauss_pivoteo(A, b)

print("\nCoeficientes del polinomio:")

for i in range(cantidad):
    print(f"a{i} = {coeficientes[i]}")


# --------------------------------------------------
# 5. MOSTRAR EL POLINOMIO
# --------------------------------------------------

polinomio = f"{coeficientes[0]:.6f}"

for i in range(1, cantidad):

    if coeficientes[i] >= 0:
        signo = "+"
    else:
        signo = "-"

    if i == 1:
        potencia = "x"
    else:
        potencia = f"x^{i}"

    polinomio += (
        f" {signo} {abs(coeficientes[i]):.6f}{potencia}"
    )

print("\nPolinomio interpolador:")
print("P(x) =", polinomio)


# --------------------------------------------------
# 6. EVALUAR EL POLINOMIO
# --------------------------------------------------

x_evaluar = float(
    input("\nIngrese el valor de x que desea interpolar: ")
    .replace(",", ".")
)

resultado = 0.0

for i in range(cantidad):
    resultado += coeficientes[i] * x_evaluar ** i

print(f"\nP({x_evaluar}) = {resultado}")
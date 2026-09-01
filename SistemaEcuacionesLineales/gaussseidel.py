import math


A = [
    [10.0, 1.0, 1.0],
    [2.0, 10.0, 1.0],
    [2.0, 2.0, 10.0]
]

b = [12.0, 13.0, 14.0]
n = len(A)

tolerancia = 1e-5
max_iteraciones = 10000


def es_diagonalmente_dominante(matriz):
    """Comprueba dominancia diagonal estricta por filas."""
    for i in range(len(matriz)):
        diagonal = abs(matriz[i][i])
        suma_no_diagonal = 0.0

        for j in range(len(matriz[i])):
            if j != i:
                suma_no_diagonal += abs(matriz[i][j])

        if diagonal <= suma_no_diagonal:
            return False

    return True


if not es_diagonalmente_dominante(A):
    print("La matriz no es diagonalmente dominante.")
    print("No se garantiza la convergencia del metodo de Gauss-Seidel.")
else:
    print("La matriz es diagonalmente dominante.")

    x_viejo = [0.0] * n
    x_nuevo = [0.0] * n
    error_nuevo = float("inf")
    error_viejo = None
    iteraciones = 0
    converge = True

    while error_nuevo > tolerancia and iteraciones < max_iteraciones:
        # Se copian los valores anteriores antes de comenzar la iteracion.
        for i in range(n):
            x_nuevo[i] = x_viejo[i]

        # En Gauss-Seidel se usa inmediatamente cada valor nuevo calculado.
        for i in range(n):
            suma = 0.0
            for j in range(n):
                if j != i:
                    suma += A[i][j] * x_nuevo[j]

            x_nuevo[i] = (b[i] - suma) / A[i][i]

        suma_error = 0.0
        for i in range(n):
            suma_error += (x_nuevo[i] - x_viejo[i]) ** 2

        error_nuevo = math.sqrt(suma_error)
        iteraciones += 1

        # En la primera iteracion todavia no existe un error anterior.
        if iteraciones == 1:
            error_viejo = error_nuevo
        elif error_viejo < error_nuevo:
            converge = False
            print("El error aumento: el metodo no converge.")
            break

        # Xv[i] = Xn[i]: la nueva aproximacion pasa a ser la anterior.
        for i in range(n):
            x_viejo[i] = x_nuevo[i]

        # El error nuevo pasa a ser el error viejo de la proxima vuelta.
        error_viejo = error_nuevo

    if converge and error_nuevo <= tolerancia:
        print("\nVector solucion:")
        for i in range(n):
            print(f"x{i + 1} = {x_nuevo[i]:.8f}")
        print(f"Numero de iteraciones: {iteraciones}")
        print(f"Error final: {error_nuevo:.8f}")
    elif converge:
        print("Se alcanzo el numero maximo de iteraciones sin converger.")

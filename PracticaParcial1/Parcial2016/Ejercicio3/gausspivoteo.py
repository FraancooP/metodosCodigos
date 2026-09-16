def gauss_pivoteo(A, b):
    # Hacemos copias para no modificar las matrices originales
    A = [fila[:] for fila in A]
    b = b[:]

    n = len(A)

    # Eliminación de Gauss con pivoteo parcial
    for i in range(n - 1):

        # Buscar la fila con el pivote más grande
        fila_pivote = i

        for fila in range(i + 1, n):
            if abs(A[fila][i]) > abs(A[fila_pivote][i]):
                fila_pivote = fila

        # Comprobar si el sistema es singular
        if abs(A[fila_pivote][i]) < 1e-12:
            raise ValueError("La matriz es singular o casi singular.")

        # Intercambiar filas
        if fila_pivote != i:
            A[i], A[fila_pivote] = A[fila_pivote], A[i]
            b[i], b[fila_pivote] = b[fila_pivote], b[i]

        # Hacer ceros debajo del pivote
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]

            for k in range(i, n):
                A[j][k] = A[j][k] - factor * A[i][k]

            b[j] = b[j] - factor * b[i]

    # Retrosustitución
    solucion = [0.0] * n

    for i in range(n - 1, -1, -1):

        if abs(A[i][i]) < 1e-12:
            raise ValueError("La matriz es singular o casi singular.")

        suma = 0.0

        for j in range(i + 1, n):
            suma = suma + A[i][j] * solucion[j]

        solucion[i] = (b[i] - suma) / A[i][i]

    return solucion
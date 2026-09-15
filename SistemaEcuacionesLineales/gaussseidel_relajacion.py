import math


A = [
    [3.0, -2.0, 1.0, 0.0, 0.0 , 0.0],
    [-2.0, 4.0, -2.0, 1.0, 0.0 , 0.0],
    [1.0, -2.0, 4.0, -2.0, 1.0 , 0.0],
    [0.0, 1.0, -2.0, 4.0, -2.0 , 1.0],
    [0.0, 0.0, 1.0, -2.0, 4.0 , -2.0],
    [0.0, 0.0, 0.0, 1.0, -2.0 , 3.0]
]

b = [10.0, -8.0, 10.0, 10.0, -8.0, 10.0]
n = len(A)

omega = 1.0
tolerancia = 1e-4
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


if not 0 < omega < 2:
    raise ValueError("Omega debe estar comprendido entre 0 y 2.")

if not es_diagonalmente_dominante(A):
    print("La matriz no es diagonalmente dominante.")
    print("No se garantiza la convergencia del metodo.")
else:
    print("La matriz es diagonalmente dominante.")

print(f"Factor de relajacion omega = {omega}")

x_viejo = [0.0] * n
x_nuevo = [0.0] * n
error_nuevo = float("inf")
error_viejo = None
iteraciones = 0
converge = True

while error_nuevo > tolerancia and iteraciones < max_iteraciones:
    # Calcular cada x nuevo.
    for i in range(n):
        suma = 0.0

        # Valores que ya calculamos dentro de esta iteracion.
        for j in range(i):
            suma += A[i][j] * x_nuevo[j]

        # Valores que todavia no calculamos.
        for j in range(i + 1, n):
            suma += A[i][j] * x_viejo[j]

        # Valor que produciria Gauss-Seidel sin relajacion.
        x_gauss_seidel = (b[i] - suma) / A[i][i]

        # Aplicar relajacion con el factor omega.
        x_nuevo[i] = ((1.0 - omega) * x_viejo[i] + omega * x_gauss_seidel)

    #suma_error = 0.0
    #for i in range(n):
    #    suma_error += (x_nuevo[i] - x_viejo[i]) ** 2

    #error_nuevo = math.sqrt(suma_error)
    
    
    
    
    # Calcular el residuo.
    suma_residual = 0.0
    for i in range(n):
        producto_fila = 0.0
        
        for j in range(n):
            producto_fila += A[i][j] * x_nuevo[j]
            
        residuo = producto_fila - b[i]
        suma_residual += residuo ** 2
        
    error_nuevo = math.sqrt(suma_residual)
    iteraciones += 1

    # En la primera iteracion todavia no existe un error anterior.
    if iteraciones == 1:
        error_viejo = error_nuevo
    elif error_viejo < error_nuevo:
        converge = False
        print("El error aumento: el metodo no converge.")
        #break

    #print(
    #    f"Iteracion {iteraciones}: x = {x_nuevo}, "
    #    f"error = {error_nuevo}"
    #)

    # Xv[i] = Xn[i]: la nueva aproximacion pasa a ser la anterior.
    for i in range(n):
        x_viejo[i] = x_nuevo[i]

    # El error nuevo pasa a ser el error viejo de la proxima vuelta.
    error_viejo = error_nuevo

if converge and error_nuevo <= tolerancia:
    print("\nVector solucion:")
    for i in range(n):
        print(f"x{i + 1} = {x_nuevo[i]}")
    print(f"Numero de iteraciones: {iteraciones}")
    print(f"Error final: {error_nuevo}")
elif converge:
    print("Se alcanzo el numero maximo de iteraciones sin converger.")

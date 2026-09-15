import math
from pathlib import Path

#A = [
#    [3.0, 1.0, 1.0],
#    [2.0, 6.0, 1.0],
#    [1.0, 1.0, 4.0]
#]

#b = [5.0, 9.0, 6.0]

#A = [
#    [5.0, 7.0, 6.0, 5.0],
#    [7.0, 10.0, 8.0, 7.0],
#    [6.0, 8.0, 10.0, 9.0],
#    [5.0, 7.0, 9.0, 10.0]
#]

#b = [23.0, 32.0, 33.0, 31.0]
n = 50
A = [[0.0] * n for _ in range(n)]
b = [5.0] * n

for i in range(n):
    for j in range(n):
        distancia_diagonal = abs(i - j)

        if distancia_diagonal == 0:
            A[i][j] = 12.0
        elif distancia_diagonal == 1:
            A[i][j] = -2.0
        elif distancia_diagonal == 2:
            A[i][j] = 1.0

# Se guarda la matriz en la misma carpeta que este programa.
ruta_matriz = Path(__file__).with_name("matriz_A.txt")
with ruta_matriz.open("w", encoding="utf-8") as archivo:
    for fila in A:
        archivo.write(" ".join(f"{valor:5.1f}" for valor in fila) + "\n")

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

ancho_banda = 0.0
for i in range(n):
    for j in range(n):
        if A[i][j] != 0:
            ancho_banda = max(ancho_banda, abs(i - j))

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
        
        inicio = max(0, i - int(ancho_banda))
        fin = min(n, i + int(ancho_banda) + 1)
        
        
        
        for j in range(inicio, fin):
            if j != i:
                suma += A[i][j] * x_nuevo[j]

        x_nuevo[i] = (b[i] - suma) / A[i][i]
        
    
    
    # Norma euclidiana entre dos aproximaciones consecutivas:
    # error_k = ||X_k - X_(k+1)||_2.
    #error_nuevo = math.sqrt(sum(
    #    (x_viejo[i] - x_nuevo[i]) ** 2 for i in range(n)
    #))
    
    
    # Norma euclidiana del residuo: ||A * x_nuevo - b||_2
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

    # Xv[i] = Xn[i]: la nueva aproximacion pasa a ser la anterior.
    for i in range(n):
        x_viejo[i] = x_nuevo[i]

    # El error nuevo pasa a ser el error viejo de la proxima vuelta.
    error_viejo = error_nuevo

    #print(f"Iteracion {iteraciones}:")
    #for i in range(n):
    #    print(f"x{i + 1} = {x_nuevo[i]}")
    #print(f"Error: {error_nuevo}\n")


if converge and error_nuevo <= tolerancia:
    print("\nVector solucion:")
    for i in range(n):
        print(f"x{i + 1} = {x_nuevo[i]}")
    print(f"Numero de iteraciones: {iteraciones}")
    print(f"Error final: {error_nuevo}")
elif converge:
    print("Se alcanzo el numero maximo de iteraciones sin converger.")

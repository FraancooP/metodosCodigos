import math


#A = [
 #   [-1.0, 1.0, -math.cos(math.radians(45.0)), 0.0, 0.0, 0.0],
  #  [0.0, 0.0, math.sin(math.radians(45.0)), 1.0, 0.0, 0.0],
   # [0.0, 0.0, 0.0, -1.0, -math.sin(math.radians(45.0)), 0.0],
    #[0.0, -1.0, 0.0, 0.0, -math.cos(math.radians(45.0)), 0.0],
    #[0.0, 0.0, 0.0, 0.0, math.sin(math.radians(45.0)), 0.0]
#]

#b = [0.0, 18.0, 0.0, 0.0, 0.0, 12.0]


#A = [
#    [80.0, -50.0, -30.0, 0.0],
#    [-50.0, 100.0, -10.0, -25.0],
#    [-30.0, -10.0, 65.0, -20.0],
#    [0.0, -25.0, -20.0, 100.0]
#]

#A = [
#    [5.0, 7.0, 6.0, 5.0],
#    [7.0, 10.0, 8.0, 7.0],
#    [6.0, 8.0, 10.0, 9.0],
#    [5.0, 7.0, 9.0, 10.0]
#]

#b = [23.0, 32.0, 33.0, 31.0]

A = [
    [33.3265,  18.997,  11.290000000000001],
    [18.997, 11.290000000000001,  7.3],
    [11.290000000000001,  7.3,  6.0]
]

b = [56.06070000000000, 31.037, 16.740000000000002]
n = len(A)
intercambios_filas = 0


sumaa = 0

for i in range(len(A)):
    for j in range(len(A)):
        sumaa += A[i][j] ** 2

norma = math.sqrt(sumaa)



#Gauss con pivoteo parcial y eliminacion=========================================
for i in range(n - 1):
    fila_pivote = i
    for fila in range(i + 1, n):
        if abs(A[fila][i]) > abs(A[fila_pivote][i]):
            fila_pivote = fila
    
    
    if abs(A[fila_pivote][i]) < 1e-12:
        print("La matriz puede ser singular o casi singular.")
        break
    
    if fila_pivote != i:
        A[i], A[fila_pivote] = A[fila_pivote], A[i]
        b[i], b[fila_pivote] = b[fila_pivote], b[i]
        intercambios_filas = intercambios_filas + 1
        
    for j in range(i + 1, n):
        factor = A[j][i] / A[i][i]
        for k in range(i, n):
            A[j][k] = A[j][k] - factor * A[i][k]
        b[j] = b[j] - factor * b[i]
#==============================================================================
            
print("Matriz triangular superior:")
for fila in A:
    print(fila)
print("Vector b modificado:")
print(b)

x = [0.0] * n
for i in range(n - 1, -1, -1):
    suma = 0.0
    for j in range(i + 1, n):
        suma = suma + A[i][j] * x[j]
    x[i] = (b[i] - suma) / A[i][i]
    
print("Vector solucion:")
for i in range(n):
    print(f"x{i+1} = {x[i]}")

# Cada intercambio de filas cambia el signo del determinante.
determinante = (-1.0) ** intercambios_filas
for i in range(n):
    determinante = determinante * A[i][i]

print(f"Determinante de A: {determinante}")
print("Norma =", norma)
